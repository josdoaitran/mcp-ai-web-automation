import flask
from flask import Flask, request, jsonify
import anthropic
import json
import base64
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

app = Flask(__name__)
client = anthropic.Anthropic(api_key="your_api_key")

# Store context between requests
context_store = {}

@app.route('/analyze', methods=['POST'])
def analyze_page():
    data = request.json
    test_id = data.get('test_id')
    page_source = data.get('page_source')
    screenshot = data.get('screenshot')
    action_request = data.get('action_request')
    
    # Retrieve or create context for this test
    if test_id not in context_store:
        context_store[test_id] = {"history": []}
    
    # Prepare the prompt for Claude
    prompt = f"""
    You are an AI test automation assistant.
    
    CURRENT PAGE:
    {page_source[:30000]}  # Limiting size
    
    ACTION REQUESTED: {action_request}
    
    Based on the page content, provide JSON with:
    1. Analysis of the page elements
    2. Suggested test actions
    3. Expected results
    4. Possible edge cases
    
    Return your response in valid JSON format only.
    """
    
    # Get Claude's analysis
    response = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=2000,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    claude_response = response.content[0].text
    
    # Try to parse as JSON
    try:
        analysis = json.loads(claude_response)
    except json.JSONDecodeError:
        # If not valid JSON, return raw text
        analysis = {"error": "Failed to parse response as JSON", "raw_response": claude_response}
    
    # Store in context history
    context_store[test_id]["history"].append({
        "action_request": action_request,
        "analysis": analysis
    })
    
    return jsonify(analysis)

@app.route('/element-finder', methods=['POST'])
def find_element():
    data = request.json
    description = data.get('description')
    page_source = data.get('page_source')
    
    prompt = f"""
    You are an AI test automation assistant.
    
    TASK: Find the best selector for the element described as: "{description}"
    
    PAGE SOURCE:
    {page_source[:30000]}
    
    Return ONLY a JSON object with these selector strategies:
    {{
      "xpath": "the xpath selector",
      "css": "the css selector",
      "id": "the id if available",
      "confidence": 0.95  // your confidence score
    }}
    """
    
    response = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=500,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    try:
        selector_data = json.loads(response.content[0].text)
        return jsonify(selector_data)
    except:
        return jsonify({"error": "Could not parse response", "raw": response.content[0].text})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
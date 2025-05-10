import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def test_iphone_browser():
    # iPhone 15 dimensions
    iphone_15_width = 393
    iphone_15_height = 852
    
    # Set up Chrome options for mobile emulation
    chrome_options = Options()
    mobile_emulation = {
        "deviceMetrics": {
            "width": iphone_15_width,
            "height": iphone_15_height,
            "pixelRatio": 3.0
        },
        "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1"
    }
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    
    # Initialize the driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    try:
        # Navigate to GitHub
        driver.get("https://github.com")
        
        # Add a small delay to ensure the page loads (optional)
        driver.implicitly_wait(3)
        
    finally:
        # Close the browser
        driver.quit()
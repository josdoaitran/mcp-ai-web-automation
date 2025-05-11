# Local Environment Setup Guide

## Prerequisites
- Python 3.7 or higher
- pip (Python package installer)
- Chrome browser installed

## Setup Steps

1. Create and activate virtual environment:
```bash
# Create a virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
.\venv\Scripts\activate
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Install Chrome WebDriver:
The Chrome WebDriver should match your Chrome browser version. You can download it from:
https://sites.google.com/chromium.org/driver/

## Project Structure
```
example-python-selenium/
├── test_github_mobile.py  # Test script
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Running the Tests
To run the tests, make sure your virtual environment is activated and run:
```bash
pytest test_github_mobile.py -v
```

## Dependencies
All required packages are listed in requirements.txt:
- pytest
- selenium
- webdriver-manager

## Troubleshooting
- Make sure Chrome browser is installed
- Verify Chrome WebDriver version matches your Chrome browser version
- Ensure all dependencies are installed correctly
- Check that virtual environment is activated before running tests
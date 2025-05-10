# iPhone 15 Browser Simulation with Selenium

This project demonstrates how to use Selenium with Python to simulate an iPhone 15 browser viewport and access GitHub.com.

## Prerequisites

- Python 3.7 or higher
- Google Chrome browser installed
- pip (Python package installer)

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- On macOS/Linux:
```bash
source venv/bin/activate
```
- On Windows:
```bash
.\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Tests

To run the test:
```bash
pytest test_iphone_browser.py -v
```

## What the Test Does

The test script will:
1. Launch Chrome browser with iPhone 15 viewport dimensions (393x852)
2. Configure mobile user agent and device metrics
3. Navigate to GitHub.com
4. Close the browser automatically after execution

## Notes

- The script uses webdriver-manager to automatically handle ChromeDriver installation
- Mobile emulation is achieved through Chrome DevTools Protocol
- The browser will close automatically even if the test fails (using try-finally)
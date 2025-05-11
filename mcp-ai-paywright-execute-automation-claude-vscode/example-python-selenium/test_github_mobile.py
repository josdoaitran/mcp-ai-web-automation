import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    # Set up Chrome options for iPhone 15 emulation
    chrome_options = Options()
    mobile_emulation = {
        "deviceMetrics": { "width": 390, "height": 844, "pixelRatio": 3.0 },
        "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1"
    }
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    
    # Initialize the driver with automatic ChromeDriver management
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    yield driver
    
    # Cleanup after test
    driver.quit()

def test_github_mobile(driver):
    # Navigate to GitHub
    driver.get("https://github.com")
    
    # Verify we're on GitHub (basic check)
    assert "GitHub" in driver.title

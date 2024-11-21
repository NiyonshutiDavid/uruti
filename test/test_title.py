from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Initialize ChromeDriver with options
driver = webdriver.Chrome(options=chrome_options)

try:
    # Open posinnove.com
    driver.get("http://uruti.rw")

    # Verify the title of the page
    assert "Uruti - Empowering Rwanda's Agritech industry" in driver.title
    print("Title check passed!")

finally:
    # Close the browser
    driver.quit()


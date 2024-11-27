from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configure WebDriver
options = Options()
options.add_argument('--headless')  # Run in headless mode
options.add_argument('--no-sandbox')  # Prevent sandboxing issues
options.add_argument('--disable-dev-shm-usage')  # Address shared memory errors
driver = webdriver.Chrome(options=options)

# Base URL of the Uruti platform
BASE_URL = "https://uruti.adaptable.app"  # Update if deployed on a different URL

def test_homepage():
    driver.get(BASE_URL)
    assert "Uruti" in driver.title, "Homepage title does not match."
    print("Homepage title test passed.")

def test_navigation_to_registration():
    driver.get(BASE_URL)
    driver.find_element(By.LINK_TEXT, "registration").click()  # Ensure there's a 'Register' link
    assert "registration" in driver.current_url, "Failed to navigate to registration page."
    print("Navigation to registration page test passed.")

def test_registration():
    driver.get(f"{BASE_URL}/registration")
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "full_name"))
        ).send_keys("John Doe")
        driver.find_element(By.NAME, "email").send_keys("johndoe@example.com")
        driver.find_element(By.NAME, "password").send_keys("password123")
        driver.find_element(By.NAME, "phone_number").send_keys("123456789")
        driver.find_element(By.NAME, "linkedin_url").send_keys("https://linkedin.com/in/johndoe")
        driver.find_element(By.NAME, "business_name").send_keys("Green Farm Co.")

        # Use Select for dropdowns
        Select(driver.find_element(By.NAME, "business_type")).select_by_visible_text("Farming")
        Select(driver.find_element(By.NAME, "business_stage")).select_by_visible_text("Idea")

        driver.find_element(By.ID, "submit-btn").click()
        
        WebDriverWait(driver, 10).until(
            EC.title_contains("Dashboard")
            );
        print("Registration of ent passed!!")
    except Exception as e:
        print(f"Registration test failed: {e}")

def test_login():
    driver.get(f"{BASE_URL}/login")
    driver.find_element(By.NAME, "email").send_keys("johndoe@example.com")
    driver.find_element(By.NAME, "password").send_keys("password123")
    driver.find_element(By.ID, "login-btn").click()  # Ensure the form has a button with id 'login-btn'
    time.sleep(2)  # Wait for potential redirection
    assert "Dashboard" in driver.title, "Login test failed."
    print("Login test passed.")

def test_logout():
    driver.find_element(By.LINK_TEXT, "Logout").click()  # Ensure there is a 'Logout' link
    time.sleep(1)
    assert "Login" in driver.title, "Logout test failed."
    print("Logout test passed.")

# Execute the test cases
try:
    test_homepage()
    test_navigation_to_registration()
    test_registration()
    test_login()
    test_logout()
finally:
    driver.quit()  # Close the browser

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Set up the Service object with the chromedriver path provided by ChromeDriverManager
service = Service(ChromeDriverManager().install())

# Set up Chrome options (optional)
options = Options()
# options.add_argument("--headless")  # Uncomment this line if you want to run Chrome in headless mode

# Initialize the WebDriver with the correct Service and Options
driver = webdriver.Chrome(service=service, options=options)

# Go to a webpage (for example, Wikipedia)
driver.get("https://en.wikipedia.org/wiki/NASA")

# Take a screenshot and save it
screenshot_path = "nasa_wikipedia_screenshot.png"
driver.save_screenshot(screenshot_path)

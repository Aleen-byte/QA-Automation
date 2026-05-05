from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def create_driver(headless=True):
    options = Options()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    # Selenium Manager (built into Selenium 4.6+) handles ChromeDriver automatically
    return webdriver.Chrome(options=options)

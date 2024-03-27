from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def before_scenario(context, scenario):
    options = Options()
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")
    options.add_argument("disable-blink-features=AutomationControlled")
    context.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    context.driver.get("https://www.cleartrip.com/")
    context.driver.maximize_window()
    context.wait = WebDriverWait(context.driver, 10)
    time.sleep(6)


def after_scenario(context, scenario):
    context.driver.quit()

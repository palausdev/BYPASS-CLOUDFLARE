from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('--disable-extensions')
options.add_argument('--no-sandbox')
options.add_argument('--disable-infobars')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-browser-side-navigation')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=options)

driver.execute_script("window.open('https://nowsecure.nl/', '_blank')")
time.sleep(15)
driver.switch_to.window(driver.window_handles[1])

driver.switch_to.frame(0)

driver.find_element(By.XPATH, '//*[@id="challenge-stage"]/div/label/input').click()
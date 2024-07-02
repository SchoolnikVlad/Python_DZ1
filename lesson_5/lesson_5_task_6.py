from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time

driver = webdriver.Chrome()

driver.get("http://the-internet.herokuapp.com/entry_ad")

sleep(3) 

driver.find_element(By.CSS_SELECTOR, ".modal-footer p").click()

sleep(2)
driver.quit()


options = Options()
driver = webdriver.Firefox(options=options)

driver.get("http://the-internet.herokuapp.com/entry_ad")

time.sleep(3)

driver.find_element(By.CSS_SELECTOR, ".modal-footer p").click()

time.sleep(2)
driver.quit()
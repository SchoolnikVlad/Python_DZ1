from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/dynamicid")

for _ in range(5):
    driver.find_element(By.CSS_SELECTOR, ".btn").click()
    sleep(2)

driver.quit()

options = Options()
driver = webdriver.Firefox(options=options)

driver.get("http://uitestingplayground.com/dynamicid")

for _ in range(5):
    driver.find_element(By.CSS_SELECTOR, ".btn").click()
    sleep(2)

driver.quit()
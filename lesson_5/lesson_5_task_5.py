from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.firefox.options import Options

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/classattr")
sleep(2)

for _ in range(3):
    button = driver.find_element(By.CSS_SELECTOR, 'button.btn-primary')
    button.click()
    
    sleep(2)
    
    alert = Alert(driver)
    alert.accept()

sleep(2)
driver.quit()

options = Options()
driver = webdriver.Firefox(options=options)

driver.get("http://uitestingplayground.com/classattr")
sleep(2)

for _ in range(3):
    button = driver.find_element(By.CSS_SELECTOR, 'button.btn-primary')
    button.click()
    
    sleep(2)
    
    alert = Alert(driver)
    alert.accept()


sleep(2)
driver.quit()
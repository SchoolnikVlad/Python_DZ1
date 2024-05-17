from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

driver = webdriver.Chrome()

driver.get("http://the-internet.herokuapp.com/login")
sleep(1)

driver.find_element(By.CSS_SELECTOR, "#username").send_keys("tomsmith")
sleep(2)

driver.find_element(By.CSS_SELECTOR, "#password").send_keys("SuperSecretPassword!")
sleep(2)

driver.find_element(By.CSS_SELECTOR, "button").send_keys(Keys.RETURN)
sleep(2)
driver.quit()


options = Options()
driver = webdriver.Firefox(options=options)

driver.get("http://the-internet.herokuapp.com/login")
sleep(1)

driver.find_element(By.CSS_SELECTOR, "#username").send_keys("tomsmith")
sleep(2)

driver.find_element(By.CSS_SELECTOR, "#password").send_keys("SuperSecretPassword!")
sleep(2)

driver.find_element(By.CSS_SELECTOR, "button").send_keys(Keys.RETURN)
sleep(2)
driver.quit()
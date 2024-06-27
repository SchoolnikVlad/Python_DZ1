from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/inputs")

input_field = driver.find_element(By.CSS_SELECTOR, "input")
sleep(1)

# Вводим 1000
input_field.send_keys("1", "0", "0", "0")
#input_field.send_keys(Keys.RETURN)
sleep(2)

input_field.clear()
sleep(1)

# Вводим 999
input_field.send_keys("999")
sleep(2)
driver.quit()
 
options = Options()
driver = webdriver.Firefox(options=options)

driver.get("https://the-internet.herokuapp.com/inputs")

input_field = driver.find_element(By.CSS_SELECTOR, "input")
sleep(1)

# Вводим 1000
input_field.send_keys("1", "0", "0", "0")
input_field.send_keys(Keys.RETURN)
sleep(2)

input_field.clear()
sleep(1)

# Вводим 999
input_field.send_keys("999")
sleep(2)
driver.quit()
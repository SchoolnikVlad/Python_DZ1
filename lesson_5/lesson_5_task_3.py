from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

driver = webdriver.Chrome()

# Открытие страницы в браузере Google chrome
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

for _ in range(5):
    driver.find_element(By.CSS_SELECTOR, "button[onclick='addElement()']").click()

sleep(2)

Delete_button = driver.find_elements(By.CSS_SELECTOR, 'button.added-manually')
print("Браузер Google Chrome, количество  кнопок 'Delete' -", len(Delete_button))

driver.quit()

options = Options()
driver = webdriver.Firefox(options=options)

# Открытие страницы в браузере Firefox
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

for _ in range(5):
    button = driver.find_element(By.CSS_SELECTOR, 'button[onclick="addElement()"]')
    button.click()

sleep(2)

Delete_button = driver.find_elements(By.CSS_SELECTOR, 'button.added-manually')
print("Браузер FireFOX, количество кнопок 'Delete' -", len(Delete_button))

driver.quit()
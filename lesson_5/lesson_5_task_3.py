from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

driver = webdriver.Chrome()

# Открытие страницы в браузере Google chrome
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

button = "div.example button"

click_button = driver.find_element(By.XPATH, button)

for new_element in range(1, 6):
    click_button.click()
    sleep(2)

delete_button = driver.find_elements(By.CSS_SELECTOR, 'button.added-manually')
print("Браузер Google Chrome, количество  кнопок 'Delete' -", len(delete_button))

driver.quit()

options = Options()
driver = webdriver.Firefox(options=options)

# Открытие страницы в браузере Firefox
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

button = "div.example button"

click_button = driver.find_element(By.XPATH, button)

for new_element in range(1, 6):
    click_button.click()
    sleep(2)

delete_button = driver.find_elements(By.CSS_SELECTOR, 'button.added-manually')
print("Браузер FireFOX, количество кнопок 'Delete' -", len(delete_button))

driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()

# Перейти на страницу http://uitestingplayground.com/textinput
driver.implicitly_wait(15)

driver.get("http://uitestingplayground.com/textinput")

input_field = driver.find_element(By.CSS_SELECTOR,"#newButtonName")

input_field.clear()

input_field.send_keys("SkyPro")

blue_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
blue_button.click()

button_text = blue_button.text
print(button_text)

driver.quit()
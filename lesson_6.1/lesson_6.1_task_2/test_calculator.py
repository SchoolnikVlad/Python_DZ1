from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
driver.set_window_size(900, 850)

delay = driver.find_element(By.CSS_SELECTOR, '#delay')
delay.clear()
time_dalay = 45
delay.send_keys(time_dalay)

driver.find_element(By.CSS_SELECTOR, '.clear').click()

buttons = driver.find_elements(By.CSS_SELECTOR, '.btn-outline-primary')

operators = driver.find_elements(By.CSS_SELECTOR, '.btn-outline-success')

buttons[0].click()

operators[0].click()

buttons[1].click()

driver.find_element(By.CSS_SELECTOR, '.btn-outline-warning').click()

waiter = WebDriverWait(driver, 5)

waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.screen'),"15")
)

result = driver.find_element(By.CSS_SELECTOR, '.screen').text

print(result)
sleep(2)

assert result == "15", "Не правильный ответ"

driver.quit()
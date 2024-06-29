import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

def login():
    driver.get('https://www.saucedemo.com/inventory.html')
    driver.find_element(By.ID,'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()

def test_add_to_card():
    login()

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "[data-test='shopping-cart-link']").click()
    driver.find_element(By.CSS_SELECTOR, "[data-test='checkout']").click()

    driver.find_element(By.ID, 'first-name').send_keys('John')
    driver.find_element(By.ID, 'last-name').send_keys('Doe')
    driver.find_element(By.ID, 'postal-code').send_keys('12345')
    driver.find_element(By.ID, 'continue').click()

    time.sleep(2)

    total = driver.find_element(By.CLASS_NAME, 'summary_total_label').text
    assert total == 'Total: $58.29'

    driver.quit()
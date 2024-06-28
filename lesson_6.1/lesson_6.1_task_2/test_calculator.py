from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from conf import *

def test_calculator_form(chrome_browser: WebDriver):
    chrome_browser.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
    # Enter 45 in the delay input field
    delay_input = chrome_browser.find_element(By.ID, "delay")
    delay_input.clear()
    delay_input.send_keys(4)
    #Click on the buttons:
    # 7
    chrome_browser.find_element(By.XPATH, "//span[text() = '8']").click()
    # +
    chrome_browser.find_element(By.XPATH, "//span[text() = '÷']").click()
    # 8
    chrome_browser.find_element(By.XPATH, "//span[text() = '2']").click()
    # =
    chrome_browser.find_element(By.XPATH, "//span[text() = '=']").click()

    # Wait for the calculation to complete
    WebDriverWait(chrome_browser, 5).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "4"))
    # Getting text meaning from result
    result_text = chrome_browser.find_element(By.CLASS_NAME, "screen").text

    # Assert that the result is 15
    assert result_text == "4"
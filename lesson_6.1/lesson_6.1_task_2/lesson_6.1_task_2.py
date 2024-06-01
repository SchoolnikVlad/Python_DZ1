import pytest
import time
from selenium import webdriver
from CalculatorPage import CalculatorPage

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_calculator(page):
    page = CalculatorPage(webdriver)

    page.open("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    page.set_delay("45")
    page.click_button("7")
    time.sleep(1)
    page.click_button("8")
    time.sleep(1)
    page.click_button("=")
    result = page.get_result()
    assert result == "15"
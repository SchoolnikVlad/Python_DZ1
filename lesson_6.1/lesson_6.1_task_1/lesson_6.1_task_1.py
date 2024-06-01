import pytest
from selenium import webdriver
from DataFormPage import DataFormPage
from ValidationPage import ValidationPage

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_fill_data_form(browser):
    data_page = DataFormPage(browser)
    validation_page = ValidationPage(browser)


    data_page.open()

    data_page.enter_first_name("Иван")
    data_page.enter_last_name("Петров")
    data_page.enter_address("Ленина, 55-3")
    data_page.enter_email("test@skypro.com")
    data_page.enter_phone_number("+7985899998787")
    data_page.enter_zip_code("")
    data_page.enter_city("Москва")
    data_page.enter_country("Россия")
    data_page.enter_job_position("QA")
    data_page.enter_company("SkyPro")

    data_page.submit_form()

    assert validation_page.is_zip_code_red()

    assert validation_page.are_other_fields_green()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

image = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.ID, "text"), 'Done!'))

third_image_src = driver.find_elements(By.TAG_NAME, "img")[2].get_attribute("src")

print(third_image_src)

driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.implicitly_wait(25)
driver.get("http://uitestingplayground.com/ajax")

blue_bt_click = driver.find_element(By.CSS_SELECTOR,"#ajaxButton").click()

content = driver.find_element(By.CSS_SELECTOR, "#content")
txt = content.find_element(By.CSS_SELECTOR, "p.bg-success").text

print(txt)

driver.quit()
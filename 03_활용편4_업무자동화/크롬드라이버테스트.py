from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()

browser.get("https://www.daum.net")
elem = browser.find_element(By.XPATH, "//*[@id='daumSearch']/fieldset/div/div/button[3]/span[2]/svg")

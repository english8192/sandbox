import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from icecream import ic

q_dict={}
contents= []
chrome_service = ChromeService(executable_path='C:\\chromedriver.exe')
driver = webdriver.Chrome(service=chrome_service)
# Step 1: Send a GET request to the webpage
driver.get("https://randomtriviagenerator.com")  # Replace with your target URL
time.sleep(2)

cards = driver.find_elements(By.CSS_SELECTOR, "md-card")
for card in cards:
    categories = card.find_elements(By.CSS_SELECTOR, "md-card-actions > button > div:nth-child(2)")
    if any(category.text == "GEOGRAPHY" for category in categories):
        content = card.find_element(By.CSS_SELECTOR, "md-card-content")
        contents.append(content)

for content in contents: 
    ic(content.text)

driver.quit()


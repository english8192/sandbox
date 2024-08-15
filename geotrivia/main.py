import os
import time
import requests
from datetime import datetime
import random
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from icecream import ic


chrome_service = ChromeService(executable_path='C:\\chromedriver.exe')
driver = webdriver.Chrome(service=chrome_service)
# Step 1: Send a GET request to the webpage
driver.get("https://randomtriviagenerator.com/category/geography")  # Replace with your target URL



refresh_button = driver.find_element(By.CSS_SELECTOR, '[class^="refresh md-fab md-button RandomQuizFormModal_refreshButton"]')
mode_button = driver.find_element(By.CSS_SELECTOR,'ion-buttons > ion-button:nth-child(1)')
q_dict={}

# mode_button.click()
# ic("mode button clicked")

time.sleep(2)

# def scrape_cards(flipper = 1, temp = None):
#     cards = driver.find_elements(By.CSS_SELECTOR, "md-card")

#     for card in cards:

#         if flipper == 1:
                
#             categories = card.find_elements(By.CSS_SELECTOR, "md-card-actions > button > div:nth-child(2)")
#             if any(category.text == "GEOGRAPHY" for category in categories):
#                 content = card.find_element(By.CSS_SELECTOR, "md-card-content")
#                 q_dict[content.text] = None
#                 temp = content.text
#                 flipper = 2
#                 #ic("Question Added")
#             else: 
#                 continue
                

#         elif flipper == 2:
#             categories = card.find_elements(By.CSS_SELECTOR, "md-card-actions > button > div:nth-child(2)")
#             if any(category.text == "GEOGRAPHY" for category in categories):
#                 content = card.find_element(By.CSS_SELECTOR, "md-card-content")
#                 q_dict[temp] = content.text
#                 flipper = 1
#                 temp = None
#                 # ic("Answer Added")

def scrape_cards(flipper = 1, temp = None):
    cards = driver.find_elements(By.CSS_SELECTOR, "md-card")

    for card in cards:

        if flipper == 1:
            content = card.find_element(By.CSS_SELECTOR, "md-card-content")
            q_dict[content.text] = None
            temp = content.text
            flipper = 2
            #ic("Question Added")         

        elif flipper == 2:
            content = card.find_element(By.CSS_SELECTOR, "md-card-content")
            q_dict[temp] = content.text
            flipper = 1
            temp = None
            # ic("Answer Added")

def scrape_list():
    list_items = driver.find_elements(By.CSS_SELECTOR, 'trivia-list')
    for _ in list_items:
        question_element = driver.find_element(By.CSS_SELECTOR, 'div[class="text-divider-question"] > p')
        answer_element = driver.find_element(By.CSS_SELECTOR, 'div[class="text-divider-answer"] > p')
        question_text = question_element.text
        answer_text = answer_element.text 
        q_dict[question_text]=answer_text
        
start_time = datetime.now()

while True:
    card = driver.find_elements(By.CSS_SELECTOR, "md-card")
    if card is not None:
        break
    print("waiting for cards")
try:
    while len(q_dict) < 5000:

        scrape_cards()
        #scrape_list()
        refresh_button.click()
        ic("—-refresh---")
        time.sleep(1)
        #ic(q_dict)
        print(f"Number of Questions: {len(q_dict)}")    
        print(((datetime.now()-start_time).total_seconds())/(len(q_dict)+0.00000001))
finally:
    with open(f'geotrivia/output{random.randint(1,99999)}.json', 'w') as file:
        json.dump(q_dict, file)
    print("output file created.")


    driver.quit()


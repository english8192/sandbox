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



with open('fishquiz/names.txt','r') as names:
    name_list = [line.strip() for line in names]
    #ic(name_list)
# Set up the WebDriver with ChromeService
chrome_service = ChromeService(executable_path='C:\\chromedriver.exe')
driver = webdriver.Chrome(service=chrome_service)

# Create a directory to save images
output_dir = 'downloaded_images'

def get_images(query):

    if query == "test":
        driver.get(f"https://www.google.com/search?q={query}&sca_esv=cd1c1d76151aa7bf&sca_upv=1&biw=1912&bih=922&udm=2&sxsrf=ADLYWIKWrlpgLytBqXYUPHUvSx2iSRJG1Q%3A1723560173443&ei=7XC7Zv7VGr-hptQPsYCemQc&ved=0ahUKEwi-gIz_mfKHAxW_kIkEHTGAJ3MQ4dUDCBA&uact=5&oq=epic+systems&gs_lp=Egxnd3Mtd2l6LXNlcnAiDGVwaWMgc3lzdGVtczILEAAYgAQYsQMYgwEyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgARI9QxQAFibDHAAeACQAQGYAawBoAHDBqoBBDEwLjK4AQPIAQD4AQGYAgugArAFwgIEECMYJ8ICChAAGIAEGEMYigXCAggQABiABBixA8ICDhAAGIAEGLEDGIMBGIoFwgIEEAAYA5gDAJIHBDEwLjGgB5ZA&sclient=gws-wiz-serp")

        time.sleep(5)
    else:
        actions = ActionChains(driver)
        # Send '/' and then Ctrl+A
        actions.send_keys('/')
        actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
        s = f"{query} fish"
        actions.send_keys(s + Keys.ENTER)
        actions.perform()
        time.sleep(5)
        # Retrieve the first five image elements
        image_elements = [i for i in driver.find_elements(By.CSS_SELECTOR, 'img') if int(i.get_attribute("width"))>46 and i.get_attribute("alt")!="Google"][0:5]

        query_dir = os.path.join(output_dir,query)  
        if not os.path.exists(query_dir):
            os.makedirs(query_dir) 

        for i, image_element in enumerate(image_elements):
        #     # Click on the image using JavaScript
            driver.execute_script("arguments[0].click();", image_element)
            time.sleep(5)  # Wait for the image to load

            # Optionally, extract the URL of the larger image
            substrings = ["data:","encrypted","gstatic","googlelogo"]
            large_image_element = [
                im for im in driver.find_elements(By.CSS_SELECTOR, 'img')
                if im.get_attribute("src") is not None and all(substring not in im.get_attribute('src') for substring in substrings)
            ]
            if large_image_element:
                large_image_url = large_image_element[0].get_attribute('src')
            else:
                continue


            try:
                response = requests.get(large_image_url, timeout=10)  # 10-second timeout
                if response.status_code == 200:
                    image_path = os.path.join(query_dir, f'{query}_{i}.jpg')
                    with open(image_path, 'wb') as file:
                        file.write(response.content)
                    print(f"Downloaded {image_path}")
                else:
                    print(f"Failed to download image for query: {query} - Status code: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Request failed for URL: {large_image_url} - {e}")
            # Go back to the search results
            driver.back()
            time.sleep(5)




for name in name_list:
    get_images(name)

driver.quit()

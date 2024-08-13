import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from icecream import ic


# Set up the WebDriver with ChromeService
chrome_service = ChromeService(executable_path='C:\\chromedriver.exe')
driver = webdriver.Chrome(service=chrome_service)

# Create a directory to save images
output_dir = 'downloaded_images'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

try:
    # Open Google Images
    #driver.get('https://images.google.com')
    driver.get('https://www.google.com/search?sca_esv=17be21ade0269849&sca_upv=1&sxsrf=ADLYWIIDmTlP1Nzv9WQegyxTdTqShQ1mhA:1723519365201&q=fish&udm=2&fbs=AEQNm0A2upiO_GHeTz6R89sNEjTHXSUfB8x3gweQ77S5CBNH1tzEOsaivoIUdA-AqC0ULxqEU6_JAVAk23cd09fLsdbCmU2G8PVUI1YBAgKBNZdMVjy5Rew_6rpX7F7cs3KBsJLBEw8LNMdCAbAPolj5sdsei2H220QWn8ah97wZZmzk57ie619ZXbkf51EPCUvHiPK_i5JHOUdvRg_rkiCDJr5CuSp2uQ&sa=X&ved=2ahUKEwjJrZr8gfGHAxVjC3kGHfnoMj8QtKgLegQICBAB')
    # # Find the search box
    # search_box = driver.find_element(By.NAME, 'q')

    # # Enter the search term
    # search_term = 'fish'
    # search_box.send_keys(search_term)
    # search_box.send_keys(Keys.RETURN)

    # # Wait for results to load
    time.sleep(2)

    # Retrieve the first five image elements
    image_elements = [i for i in driver.find_elements(By.CSS_SELECTOR, 'img') if int(i.get_attribute("width"))>46 and i.get_attribute("alt")!="Google"][0:5]
    if image_elements:
        print("images found")
        for i in image_elements:
            print(i.get_attribute("alt"))
            
    

    for i, image_element in enumerate(image_elements):
    #     # Click on the image using JavaScript
        driver.execute_script("arguments[0].click();", image_element)
        time.sleep(2)  # Wait for the image to load

        # Optionally, extract the URL of the larger image
        large_image_element = [im for im in driver.find_elements(By.CSS_SELECTOR, 'img') if "data:" not in im.get_attribute('src')] 
        large_image_url = large_image_element[0].get_attribute('src')
        ic(large_image_url)
        
    #     # Download the image
    #     response = requests.get(large_image_url)
    #     if response.status_code == 200:
    #         image_path = os.path.join(output_dir, f'image_{i+1}.jpg')
    #         with open(image_path, 'wb') as file:
    #             file.write(response.content)
    #         print(f"Downloaded {image_path}")

    #     # Go back to the search results
    #     driver.back()
    #     time.sleep(2)

finally:
    # Close the WebDriver
    driver.quit()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Set up the WebDriver (Make sure to set the path to your WebDriver executable)
driver = webdriver.Chrome()  # Replace with your browser choice (e.g., webdriver.Firefox())
driver.get("https://geography-game.com/")

# Wait for the page to fully load
time.sleep(15)
llist=[]
# Perform the initial sequence (Tab 7 times and Enter)
body = driver.find_element(By.TAG_NAME, "body")
x = driver.find_element(By.ID, "region_select")
x.click()
y = driver.find_element(By.CSS_SELECTOR, 'option[value="9"]')

select = Select(x)

# Select an option by visible text
select.select_by_visible_text("All Oceans")  
time.sleep(5)

# Tab 2 times and Enter
for _ in range(2):
    body.send_keys(Keys.TAB)
    time.sleep(2)
time.sleep(2)
body.send_keys(Keys.ENTER)
print("Enter the game")
time.sleep(10)
# Repeated action
for _ in range(200):

    # Get the text from the h2 element with ID "target_territory_name"
    territory_name = driver.find_element(By.ID, "target_territory_name").text
    print(f"Territory name: {territory_name}")
    llist.append(territory_name)
    # Click the button with ID "skip"
    skip_button = driver.find_element(By.ID, "skip")
    skip_button.click()

    # Wait a bit to ensure the next territory is loaded
    time.sleep(0.3)

print(set(llist))
# Close the WebDriver
driver.quit()

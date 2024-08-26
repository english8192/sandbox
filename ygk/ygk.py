import requests
from bs4 import BeautifulSoup

# Replace this URL with the page you want to scrape
url = 'https://www.naqt.com/you-gotta-know/by-category.jsp#intro'

# Send a GET request to the webpage
response = requests.get(url)

# Parse the content of the webpage with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all <a> tags and extract their href attributes
hrefs = []
for a_tag in soup.find_all('a', href=True):
    hrefs.append(a_tag['href'])

# Save the hrefs into a text file
with open('ygk/hrefs.txt', 'w') as file:
    for href in hrefs:
        file.write(href + '\n')

print(f'Successfully saved {len(hrefs)} hrefs to hrefs.txt')

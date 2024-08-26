import requests
from bs4 import BeautifulSoup
import re
import os
import json

def scrape_el_from_links(input_file):
    try:
        # Read URLs from the input text file
        with open(input_file, 'r') as file:
            urls = file.read().splitlines()
        
        # Ensure the output directory exists
        os.makedirs("ygk/files", exist_ok=True)

        for url in urls:
            try:
                # Send a GET request to each URL
                response = requests.get(url)
                response.raise_for_status()  # Check if the request was successful

                # Parse the content of the webpage with BeautifulSoup
                soup = BeautifulSoup(response.content, 'html.parser')

                # Find all <li> elements within <ul> elements with class "ygk"
                elements = soup.select('ul.ygk > li')

                # Prepare a dictionary to store the scraped data
                scraped_data = {}

                for el in elements:
                    label = el.find('span', class_='label')
                    if label:
                        key = label.get_text(strip=True)
                        # Get all text inside the <li> except the label
                        value = el.get_text(strip=True).replace(key, '', 1).strip()
                        scraped_data[key] = value

                # Extract the part of the URL to use as the filename
                filename = re.search(r'\/([a-zA-Z0-9-]+)\.html$', url).group(1)
                output_file = f"ygk/files/{filename}.json"

                # Save the dictionary as a JSON file
                with open(output_file, 'w', encoding='utf-8') as file:
                    json.dump(scraped_data, file, indent=4, ensure_ascii=False)

                print(f'Successfully saved {len(scraped_data)} items to {output_file}')

            except requests.exceptions.RequestException as e:
                print(f"Failed to fetch {url}: {e}")

    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")

# Example usage
scrape_el_from_links('ygk/hrefs.txt')

import requests
from bs4 import BeautifulSoup
import json
from icecream import ic
import re


def extract_category_dollar_value(text):
    match = re.search(r'^(.*?)(?:\$(\d+)):', text)
    if match:
        category = match.group(1).strip()
        dollar_value = match.group(2) if match.group(2) else 'Unknown'
        return category, dollar_value
    return 'Unknown', 'Unknown'

def clean_question_text(question_text, answer_text):

    # Remove any occurrence of the answer text from the question text
    question_text_cleaned1 = re.sub(r'^\s*.*?\$(\d+):', '', question_text).strip()
    question_text_cleaned2 = re.sub(re.escape(answer_text), '', question_text_cleaned1).strip()
    return question_text_cleaned2

def scrape_questions(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    questions = []

    # Locate the content div
    content_div = soup.find('div', id='content')
    if not content_div:
        print("Content div not found")
        return questions

    # Find the first table under the content div
    table = content_div.find('table')
    if not table:
        print("Table not found")
        return questions

    # Attempt to find tbody, otherwise use rows directly under table
    tbody = table.find('tbody')
    if tbody:
        rows = tbody.find_all('tr')
    else:
        rows = table.find_all('tr')
    
    if not rows:
        print("No rows found")
        return questions

    for row in rows:
        # Find all <td> elements with valign='top'
        td_cells = row.find_all('td', valign='top')
        if len(td_cells) >= 2:
            # Extract the question text from the second <td>
            question_text = td_cells[1].get_text(strip=True)
            
            # Extract the answer text from the span within the same row
            answer_span = row.find('span', class_='search_correct_response')
            if answer_span:
                answer_text = answer_span.get_text(strip=True)
                
                # Extract category and dollar value
                category, dollar_value = extract_category_dollar_value(question_text)
                
                # Clean up the question text
                question_text_cleaned = clean_question_text(question_text, answer_text)

                questions.append({
                    'category': category,
                    'dollar_value': dollar_value,
                    'question': question_text_cleaned,
                    'answer': answer_text
                })
                
        else:
            print("Not enough td cells with valign='top' in row")
    ic(questions[0])
    return questions
def main():
    url = 'https://j-archive.com/search.php?search=geography&submit=Search'
    questions = scrape_questions(url)
    
    # Save the scraped questions to a JSON file
    with open('jarch/questions.json', 'w') as f:
        json.dump(questions, f, indent=4)

if __name__ == '__main__':
    main()

import requests
from lxml import html
import urllib3
import json
import csv
from typing import List, Optional, Dict
from requests.models import Response
from lxml.html import HtmlElement


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

session = requests.Session()

def get_data(url: str, xpath: str) -> Optional[List[Dict[str, str]]]:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    session.headers.update(headers)

    try:
        response: Response = session.get(url, verify=False)
        response.raise_for_status()  
        tree = html.fromstring(response.content) 
 
        results = tree.xpath(xpath)

        if isinstance(results, list):
            elements = []
            for result in results:
                if isinstance(result, HtmlElement):
                    elements.append({
                        'text': result.text_content().strip(),  
                    })
                else:
                    print(f"Skipping non-element result: {result!r}")
            return elements
        else:
            print("\nElement not found with XPath.")
            return None

    except requests.RequestException as e:
        print(f"Error making the request: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def save_to_json(data: List[Dict[str, str]], filename: str) -> None:
    """Save the extracted data to a JSON file."""
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def save_to_csv(data: List[Dict[str, str]], filename: str) -> None:
    """Save the extracted data to a CSV file."""
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['text'])
        writer.writeheader()  
        for item in data:
            writer.writerow(item)  

 
url = 'https://dockerlabs.es/'

 
xpath = '/html/body/div/div[2]/div[1]/div/span[1]/strong | /html/body/div/div[2]/div[2]//span[1]/strong'

 
result = get_data(url, xpath)

if result:
    print("\nDockerlabs Scraping")
    for idx, item in enumerate(result, start=1):
        print(f"\nDocker Name {idx}:")
        print(f" {item['text']}")
 
    save_to_json(result, 'dockerlabs_data.json')
    print("\nData saved in 'dockerlabs_data.json'.")
    
    save_to_csv(result, 'dockerlabs_data.csv')
    print("\nData saved in 'dockerlabs_data.csv'.")
else:
    print("\nNo results found.")

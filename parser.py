import json
import requests
from bs4 import BeautifulSoup

def extracting_quotes(address):

    server_response = requests.get(address)
    file_html = BeautifulSoup(server_response.text, 'html.parser')
    all_quotes = file_html.find_all('div', class_='quote')

    quotes_list = []

    for count in all_quotes:
        text_quote = count.find('span', class_='text').text.strip()
        autor_quote = count.find('small', class_='author').text
        tag_quote =[tag.text for tag in count.find_all('a', class_='tag')]

        quotes_dictionary = {
            'text' : text_quote,
            'autor' : autor_quote,
            'tag' : tag_quote
        }

        quotes_list.append(quotes_dictionary)

    return quotes_list

url = 'https://quotes.toscrape.com/'

quotes = extracting_quotes(url)

with open('qutes_parser/quotes.json', 'w', encoding='utf-8') as file:
    json.dump(quotes, file, indent=4, ensure_ascii=False)

print('"Данные сохранены в файл quotes.json')

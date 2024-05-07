from bs4 import BeautifulSoup
import requests
from time import sleep


def get_links_to_pages_cyberleninka(list_query):
    links = set()

    for q in list_query:
        response = requests.post(url='https://cyberleninka.ru/api/search', json={
            'mode': 'articles', 'q': q, 'size': 100, 'from': 0,
        })
        results = response.json()

        num_articles = len(results['articles'])

        for i in range(num_articles):
            links.add('https://cyberleninka.ru' + str(results['articles'][i]['link']))

    return list(links)


def web_page_parser_cyberleninka(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('meta', {'name': 'citation_title'})['content']
    authors = soup.find_all('meta', {'name': 'citation_author'})
    author = ''

    for a in authors:
        author += str(a['content']) + ', '

    author = author[:-2]
    abstract = soup.find('meta', {'name': 'description'})['content']
    text = soup.find('div', {'class': 'ocr'}).get_text()
    link = url

    return {
        'title': title,
        'author': author,
        'abstract': abstract,
        'text': text,
        'link': link
    }


def parser_cyberleninka(list_query):
    links = get_links_to_pages_cyberleninka(list_query)
    articles = []
    time = 5
    for url in links:
        try:
            articles.append(web_page_parser_cyberleninka(url))
        except:
            sleep(time)
            time += 1
    return articles


list_query = ['биоинспирированные алгоритмы методы', 'криптоанализ', 'биоинспирированные алгоритмы методы криптоанализ']
list_articles = parser_cyberleninka(list_query)
print(list_articles)

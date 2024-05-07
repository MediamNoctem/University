from django.shortcuts import render
from .models import Article
from bs4 import BeautifulSoup
import requests
from time import sleep

list_query = ['биоинспирированные алгоритмы методы', 'криптоанализ', 'биоинспирированные алгоритмы методы криптоанализ']

def index(request):
    # Article.objects.all().delete()
    list_articles = parser_cyberleninka(list_query)
    add_articles_to_db(list_articles)
    articles = Article.objects.all()
    return render(request, 'main/index.html', {'articles': articles})


# def parser_articles(url):
#     try:
#         response = requests.get(url)
#         soup = BeautifulSoup(response.text, 'html.parser')
#
#         title = soup.find('h1', {'class': 'tp-post-single-header__title'}).get_text()
#         author = soup.find('a', {'class': 'tp-author__link'}).get_text()
#         abstract = soup.find('p', {'class': 'tp-post-single-header__exert'}).get_text()
#         text = soup.find('div', {'class': 'tp-content-viewer'}).get_text()
#         link = soup.find('link', {'rel': 'canonical'})['href']
#
#         return {
#             'title': title,
#             'author': author,
#             'abstract': abstract,
#             'text': text,
#             'link': link
#         }
#     except Exception as e:
#         print("Ошибка: ", e)
#
#
# # https://tproger.ru/search?searchid=2415386&text=криптография&web=0
# def take_links(urls):
#     href = []
#     for url in urls:
#         response = requests.get(url)
#         soup = BeautifulSoup(response.text, 'html.parser')
#         articles = soup.find_all('a', {'class': 'b-serp-item__title-link'})
#         for article in articles:
#             href.append('https://habr.com' + article.get('href'))
#     return href
#
#
# def start(url):
#     urls = [url + '#p=' + str(page) for page in range(1, 10)]
#
#     articles_urls = take_links(urls)

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


def add_articles_to_db(articles):
    # conn = sqlite3.connect('db.sqlite3')
    # c = conn.cursor()
    # c.execute('''INSERT INTO articles (title, author, abstract, text, link) VALUES (, ?, ?, ?, ?, ?)''')
    #
    # conn.commit()
    # conn.close()
    for a in articles:
        article = Article(title=a['title'], author=a['author'], abstract=a['abstract'], text=a['text'], link=a['link'])
        article.save()

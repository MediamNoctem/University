from django.shortcuts import render
from .models import Article
from bs4 import BeautifulSoup
import requests


def index(request):
    article = Article()
    articles = Article.objects.all()
    return render(request, 'main/index.html', {'articles': articles})


def parser_articles(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.find('h1', {'class': 'tp-post-single-header__title'}).get_text()
        author = soup.find('a', {'class': 'tp-author__link'}).get_text()
        abstract = soup.find('p', {'class': 'tp-post-single-header__exert'}).get_text()
        text = soup.find('div', {'class': 'tp-content-viewer'}).get_text()
        link = soup.find('link', {'rel': 'canonical'})['href']

        return {
            'title': title,
            'author': author,
            'abstract': abstract,
            'text': text,
            'link': link
        }
    except Exception as e:
        print("Ошибка: ", e)


# https://tproger.ru/search?searchid=2415386&text=криптография&web=0
def take_links(urls):
    href = []
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('a', {'class': 'b-serp-item__title-link'})
        for article in articles:
            href.append('https://habr.com' + article.get('href'))
    return href


def start(url):
    urls = [url + '#p=' + str(page) for page in range(1, 10)]

    articles_urls = take_links(urls)

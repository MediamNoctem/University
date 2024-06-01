from django.shortcuts import render
from django.db import connection
from .models import Article
from bs4 import BeautifulSoup
import requests
from time import sleep
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import ComplementNB
from sklearn.feature_extraction.text import TfidfVectorizer

list_query = ['биоинспирированные алгоритмы методы криптоанализ']


def index(request):
    # Article.objects.all().delete()
    # list_articles = parser_cyberleninka(list_query)
    # add_articles_to_db(list_articles)
    articles = Article.objects.all()
    NB_classifier()
    return render(request, 'main/index.html', {'articles': articles})


def get_links_to_pages_cyberleninka(list_query):
    links = set()

    for q in list_query:
        response = requests.post(url='https://cyberleninka.ru/api/search', json={
            'mode': 'articles', 'q': q, 'size': 100, 'from': 0
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
    for a in articles:
        article = Article(title=a['title'], author=a['author'], abstract=a['abstract'], text=a['text'], link=a['link'])
        article.save()


def NB_classifier():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM main_article")
        data = cursor.fetchall()

    x = [column[4] for column in data]
    y = [column[-1] for column in data]

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
    # x_train = np.array(x_train)

    vectorizer = TfidfVectorizer()

    x_train_vectorized = vectorizer.fit_transform(x_train)
    x_test_vectorized = vectorizer.transform(x_test)

    classifier = ComplementNB()

    classifier.fit(x_train_vectorized, y_train)

    y_pred = classifier.predict(x_test_vectorized)

    accuracy = accuracy_score(y_test, y_pred)
    print("Точность: {:.2f}%".format(accuracy * 100))

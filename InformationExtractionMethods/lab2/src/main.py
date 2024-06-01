from bs4 import BeautifulSoup
import requests
import sqlite3
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import ComplementNB
from sklearn.feature_extraction.text import CountVectorizer


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


def NB_classifier():
    connection = sqlite3.connect('db.sqlite3')
    cursor = connection.cursor()

    cursor.execute("SELECT text FROM main_article")
    x = [i[0] for i in cursor.fetchall()]

    cursor.execute("SELECT class_affiliation FROM main_article")
    y = [i[0] for i in cursor.fetchall()]

    cursor.close()
    connection.close()

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    vectorizer = CountVectorizer()

    x_train_vectorized = vectorizer.fit_transform(x_train)
    x_test_vectorized = vectorizer.transform(x_test)

    classifier = ComplementNB()

    classifier.fit(x_train_vectorized, y_train)

    y_pred = classifier.predict(x_test_vectorized)

    accuracy = accuracy_score(y_test, y_pred)

    print("Точность: {:.2f}%".format(accuracy * 100))

    url = input('Введите url статьи с Cyberleninka: ')
    data_article = web_page_parser_cyberleninka(url)

    x_vectorized = vectorizer.transform([data_article['text']])

    prediction = classifier.predict(x_vectorized)

    if prediction[0] == 1:
        print('Статья соответствует теме магистерской работы')
    else:
        print('Статья не соответствует теме магистерской работы')


if __name__ == '__main__':
    NB_classifier()

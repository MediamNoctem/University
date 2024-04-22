from bs4 import BeautifulSoup
import requests
import httpx


def parser_articles(url):
    # try:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(type(soup))

    title = soup.find('h1', {'class': 'tp-post-single-header__title'}).get_text()
    print(title)
    author = soup.find('a', {'class': 'tp-author__link'}).get_text()
    print(author)
    abstract = soup.find('p', {'class': 'tp-post-single-header__exert'}).get_text()
    print(abstract)
    text = soup.find('div', {'class': 'tp-content-viewer'}).get_text()
    print(text)
    link = soup.find('link', {'rel': 'canonical'})['href']
    print(link)


def take_links(urls):
    links = []
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup)
        articles = soup.find('ul', {'id': 'search-results'})
        # print(articles.text)
        for article in articles:
            # print(article.get('href'))
            links.append(article.get('href'))
        # print(links)
    return links


def start(url):
    urls = [url + str(page) for page in range(1, 2)]

    articles_urls = take_links(urls)


start('https://cyberleninka.ru/search?q=криптоанализ&page=')

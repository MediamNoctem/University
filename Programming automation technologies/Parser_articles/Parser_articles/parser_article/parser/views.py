from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .forms import SearchForm
from .models import Article
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


def homepage(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search_query = form.cleaned_data['search_query']
            results = search_articles(search_query)
            return render(request, 'parser/results.html', {'results': results})
    else:
        form = SearchForm()
    return render(request, 'parser/homepage.html', {'form': form})


def search_articles(search_query):
    """
    Функция для поиска статей. Здесь будет ваша логика парсинга.
    """
    # Пример с использованием поискового запроса на arXiv
    base_url = "https://arxiv.org/search/?query="
    url = base_url + search_query
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = []
        for result in soup.find_all('li', class_='arxiv-result'):
            title_element = result.find('p', class_='title')
            authors_element = result.find('p', class_='authors')
            date_element = result.find('p', class_='is-size-7')
            abstract_element = result.find('span', class_='abstract-full')
            link_element = result.find('a', class_='link')

            title = title_element.text.strip() if title_element else "Нет названия"
            authors = authors_element.text.strip() if authors_element else "Нет авторов"
            date_str = date_element.text.split(': ')[1].strip() if date_element else None
            if date_str:
                date_obj = datetime.strptime(date_str, '%d %B %Y').date()
            else:
                date_obj = None
            abstract = abstract_element.text.strip() if abstract_element else "Нет аннотации"
            link = "https://arxiv.org" + link_element['href'] if link_element else ""

            article = {
                'title': title,
                'authors': authors,
                'date_published': date_obj,
                'abstract': abstract,
                'source_url': link,
            }
            articles.append(article)
        return articles

    except requests.exceptions.RequestException as e:
        logger.error(f"Error during request: {e}")
        return []


def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'parser/article_detail.html', {'article': article})


def save_article(request, article_data):
    try:
        article = Article(
            title=article_data['title'],
            authors=article_data['authors'],
            date_published=article_data['date_published'],
            abstract=article_data['abstract'],
            source_url=article_data['source_url'],
        )
        article.save()
        return HttpResponse("Article saved", status=200)
    except Exception as e:
        return HttpResponse(f"Error saving article {str(e)}", status=500)

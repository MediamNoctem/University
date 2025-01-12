from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('results/', views.save_article, name='results')

]

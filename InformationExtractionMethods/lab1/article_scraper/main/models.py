from django.db import models


class Article(models.Model):
    title = models.TextField('Заголовок')
    author = models.TextField('Автор')
    abstract = models.TextField('Аннотация')
    text = models.TextField('Текст статьи')
    link = models.TextField('Ссылка на источник')

    def __str__(self):
        return self.title

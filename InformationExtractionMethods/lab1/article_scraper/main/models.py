from django.db import models


class Article(models.Model):
    title = models.TextField(verbose_name='Заголовок')
    author = models.TextField(verbose_name='Автор')
    abstract = models.TextField(verbose_name='Аннотация')
    text = models.TextField(verbose_name='Текст статьи')
    link = models.TextField(verbose_name='Ссылка на источник')
    class_affiliation = models.BooleanField(verbose_name='Принадлежность классу темы курсовой', default=False)

    def __str__(self):
        return self.title

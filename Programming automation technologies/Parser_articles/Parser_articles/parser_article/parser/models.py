from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=500)
    authors = models.CharField(max_length=500)
    date_published = models.DateField(null=True, blank=True)
    abstract = models.TextField(null=True, blank=True)
    text = models.TextField()
    source_url = models.URLField()

    def __str__(self):
        return self.title

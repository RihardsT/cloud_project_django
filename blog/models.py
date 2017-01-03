from django.db import models

# Create your models here.
class Article(models.Model):
    article_title_text = models.CharField(max_length=200)
    article_content = models.TextField()
    date_published = models.DateTimeField('date published')
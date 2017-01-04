import datetime

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    article_title_text = models.CharField(max_length=200)
    article_content = models.TextField()
    date_published = models.DateTimeField('date published')
    def __str__(self):
        return self.article_content
    def was_published_recently(self):
        return self.date_published >= timezone.now() - datetime.timedelta(days=1)
import datetime

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    article_title_text = models.CharField(max_length=200)
    article_content = models.TextField()
    date_published = models.DateTimeField('date published')
    likes = models.IntegerField(default=0)
    def __str__(self):
        return self.article_title_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date_published <= now
    was_published_recently.admin_order_field = 'date_published'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
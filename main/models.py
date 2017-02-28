from django.db import models

# Create your models here.

class PageDescription(models.Model):
    page_description = models.TextField()
    display_on_page = models.CharField(max_length=200)
    def __str__(self):
        return self.page_description
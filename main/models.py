from django.db import models

# Create your models here.

class Welcome(models.Model):
    welcome_text = models.TextField()
    display_on_page = models.CharField(max_length=200)
    def __str__(self):
        return self.welcome_text
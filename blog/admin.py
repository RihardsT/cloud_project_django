from django.contrib import admin

# Register your models here.
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['article_title_text', 'article_content']}),
        ('Date information', {'fields': ['date_published'], 'classes': ['collapse']}),
    ]
    # fields = ['date_published', 'article_title_text', 'article_content']
    list_display = ('article_title_text', 'date_published', 'was_published_recently')
    list_filter = ['date_published']
    search_fields = ['article_title_text']

admin.site.register(Article, ArticleAdmin)

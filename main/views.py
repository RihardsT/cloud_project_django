from django.shortcuts import render
from django.views.generic.base import TemplateView

from blog.models import Article

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'main/index.html'
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['latest_article'] = Article.objects.last()
        return context
from django.shortcuts import render
from django.http import HttpResponse

from .models import Article

# Create your views here.
def index(request):
    latest_article_list = Article.objects.order_by('-date_published')[:5]
    context = {'latest_article_list': latest_article_list }
    return render(request, 'blog/index.html', context)


def detail(request, article_id):
    return HttpResponse("You're looking at article %s." % article_id)

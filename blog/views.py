from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Article

# Create your views here.
def index(request):
    latest_article_list = Article.objects.order_by('-date_published')[:5]
    # output = ', '.join([a.article_title_text for a in latest_article_list])
    # return HttpResponse(output)
    template = loader.get_template('blog/index.html')
    context = {
        'latest_article_list': latest_article_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, article_id):
    return HttpResponse("You're looking at article %s." % article_id)

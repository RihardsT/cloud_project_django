from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Article

# Create your views here.
def index(request):
    latest_article_list = Article.objects.order_by('-date_published')[:5]
    context = {'latest_article_list': latest_article_list }
    return render(request, 'blog/index.html', context)


def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'blog/detail.html', {'article': article})

def like(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    try:
        article.likes += 1
        article.save()
    except (KeyError, Article.DoesNotExist):
        # Redisplay the article like form.
        return render(request, 'blog/detail.html', {
            'article': article,
            'error_message': "You didn't select like.",
        })
    else:
        # article.likes += 1
        # article.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('blog:detail', args=(article.id,)))
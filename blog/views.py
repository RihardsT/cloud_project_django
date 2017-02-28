from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Article
from main.models import PageDescription

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_article_list'
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        page_description = PageDescription.objects.filter(display_on_page="blog").first()
        if page_description is not None:
            context['page_description'] = page_description
        return context
    def get_queryset(self):
        """
        Return the last five published articles (not including those set to be
        published in the future).
        """
        return Article.objects.filter(
            date_published__lte=timezone.now()
        ).order_by('-date_published')[:5]

class DetailView(generic.DetailView):
    model = Article
    template_name = 'blog/detail.html'

    def get_queryset(self):
        """
        Excludes any articles that aren't published yet.
        """
        return Article.objects.filter(date_published__lte=timezone.now())

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
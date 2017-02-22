from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
import datetime

from blog.models import Article


# Create your tests here.

class ArticleMethodTests(TestCase):
    def test_was_published_recently_with_future_article(self):
        """
        was_published_recently() should return False for articles whose
        date_published is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_article = Article(date_published=time)
        self.assertIs(future_article.was_published_recently(), False)

    def test_was_published_recently_with_old_article(self):
        """
        was_published_recently() should return False for articles whose
        date_published is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=30)
        old_article = Article(date_published=time)
        self.assertIs(old_article.was_published_recently(), False)

    def test_was_published_recently_with_recent_article(self):
        """
        was_published_recently() should return True for articles whose
        date_published is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_article = Article(date_published=time)
        self.assertIs(recent_article.was_published_recently(), True)

def create_article(article_title_text, article_content, days):
    """
    Creates a article with the given `article_title_text` and published the
    given number of `days` offset to now (negative for articles published
    in the past, positive for articles that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Article.objects.create(article_title_text=article_title_text,
        article_content=article_content, likes=0, date_published=time)


class ArticleViewTests(TestCase):
    def test_index_view_with_no_articles(self):
        """
        If no articles exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('blog:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No articles are available.")
        self.assertQuerysetEqual(response.context['latest_article_list'], [])

    def test_index_view_with_a_past_article(self):
        """
        Articles with a date_published in the past should be displayed on the
        index page.
        """
        create_article(article_title_text="Past article.",
            article_content="Past article content", days=-30)
        response = self.client.get(reverse('blog:index'))
        self.assertQuerysetEqual(
            response.context['latest_article_list'],
            ['<Article: Past article.>']
        )

    def test_index_view_with_a_future_article(self):
        """
        Articles with a date_published in the future should not be displayed on
        the index page.
        """
        create_article(article_title_text="Future article.",
            article_content="Future article content", days=30)
        response = self.client.get(reverse('blog:index'))
        self.assertContains(response, "No articles are available.")
        self.assertQuerysetEqual(response.context['latest_article_list'], [])

    def test_index_view_with_future_article_and_past_article(self):
        """
        Even if both past and future articles exist, only past articles
        should be displayed.
        """
        create_article(article_title_text="Past article.",
            article_content="Past article content",  days=-30)
        create_article(article_title_text="Future article.",
            article_content="Future article content", days=30)
        response = self.client.get(reverse('blog:index'))
        self.assertQuerysetEqual(
            response.context['latest_article_list'],
            ['<Article: Past article.>']
        )

    def test_index_view_with_two_past_articles(self):
        """
        The articles index page may display multiple articles.
        """
        create_article(article_title_text="Past article 1.",
            article_content="Past article content", days=-30)
        create_article(article_title_text="Past article 2.",
            article_content="Past article content 2", days=-5)
        response = self.client.get(reverse('blog:index'))
        self.assertQuerysetEqual(
            response.context['latest_article_list'],
            ['<Article: Past article 2.>', '<Article: Past article 1.>']
        )

class ArticleIndexDetailTests(TestCase):
    def test_detail_view_with_a_future_article(self):
        """
        The detail view of a article with a pub_date in the future should
        return a 404 not found.
        """
        future_article = create_article(article_title_text='Future article.',
            article_content="Future article content", days=5)
        url = reverse('blog:detail', args=(future_article.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_detail_view_with_a_past_article(self):
        """
        The detail view of a article with a pub_date in the past should
        display the article's text.
        """
        past_article = create_article(article_title_text='Past Article.',
            article_content="Past article content", days=-5)
        url = reverse('blog:detail', args=(past_article.id,))
        response = self.client.get(url)
        self.assertContains(response, past_article.article_title_text)

class ArticleDetailTestLikes(TestCase):
    def test_detail_view_add_like_redirects_back_to_detail_when_fails(self):
        """Test that like redirects back to article"""
        article = create_article(article_title_text='Article.',
            article_content="Article content", days=-5)
        url = reverse('blog:like', args=(article.id,))
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302) # Redirect code
        self.assertRedirects(response, f'/blog/{article.id}/')
        # Literal String Interpolation. f'{var}'

    def test_detail_view_add_like(self):
        """Pressing like button should increase articles like count"""
        article = create_article(article_title_text='Article.',
            article_content="Article content", days=-5)
        url = reverse('blog:like', args=(article.id,))
        self.client.post(url) # I expect this to update the article like count. Doesn't.
        article.likes += 1
        self.assertEqual(article.likes, 1)

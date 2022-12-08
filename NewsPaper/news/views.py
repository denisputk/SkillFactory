from django.views.generic import ListView, DetailView
from .models import Post


class NewsList(ListView):
    model = Post
    ordering = '-post_created'
    template_name = 'News.html'
    context_object_name = 'news'


class NewsDetail(DetailView):
    model = Post
    template_name = 'sep_news.html'
    context_object_name = 'sep_news'

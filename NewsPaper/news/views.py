from django.views.generic import ListView, DetailView
from .models import Post


class NewsList(ListView):
    model = Post
    ordering = '-time_create'
    template_name = 'all_news.html'
    context_object_name = 'all_news'


class NewsDetail(DetailView):
    model = Post
    template_name = 'one_news.html'
    context_object_name = 'one_news'
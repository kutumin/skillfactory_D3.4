#from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
# Create your views here.

class PostList(ListView):
    model = Post
    template_name = 'news.html' 
    context_object_name = 'news'
    queryset = Post.objects.filter(post_type='news').values_list('id', flat=True).order_by('-id')

class PostDetail(DetailView):
    model = Post
    template_name = 'details_news.html' 
    context_object_name = 'news'
    queryset = Post.objects.filter(post_type='news')
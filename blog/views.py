from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


# def blog(request):
#     return render(request, 'blog.html', {})

class BlogView(ListView):
    model = Post
    template_name = 'blog.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

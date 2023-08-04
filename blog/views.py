from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post


# def blog(request):
#     return render(request, 'blog.html', {})

class BlogView(ListView):
    model = Post
    template_name = 'blog.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__'


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    fields = ['title', 'body']
    
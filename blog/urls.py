from django.urls import path
from .views import BlogView, PostDetailView, AddPostView, UpdatePostView

urlpatterns = [
    path('', BlogView.as_view(), name="blog"),
    path('article/<int:pk>', PostDetailView.as_view(), name="post_detail"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('edit_post/<int:pk>', UpdatePostView.as_view(), name="edit_post"),
]

from django.urls import path
from .views import PostList, PostDetailView, AddPostView, UpdatePostView, DeletePostView

urlpatterns = [
    path('', PostList.as_view(), name="blog"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('edit_post/<int:pk>', UpdatePostView.as_view(), name="edit_post"),
    path('delete_post/<int:pk>', DeletePostView.as_view(), name="delete_post"),
    path('article/<int:pk>', PostDetailView.as_view(), name="post_detail"),
]

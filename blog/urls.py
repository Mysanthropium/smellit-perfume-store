from django.urls import path
from .views import BlogView, PostDetailView

urlpatterns = [
    path('', BlogView.as_view(), name="blog"),
    path('article/<int:pk>', PostDetailView.as_view(), name="post_detail"),
]

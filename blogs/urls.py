from django.urls import path

from blogs.views import BlogDetailView, BlogListView

urlpatterns = [
    path('', BlogListView.as_view(), name='blog-list'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
]

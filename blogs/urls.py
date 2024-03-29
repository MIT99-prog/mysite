from django.urls import path
from django.urls.conf import include
from django.contrib import admin
from blogs.views import (
 detail, about, CategoryListView, TagListView, TagBlogView, 
 CategoryBlogView, IndexView, SearchPostView,)

app_name = 'blogs'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('detail/<int:blog_id>/', detail, name='detail'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('tags/', TagListView.as_view(), name='tag_list'),
    path('category/<str:category_slug>/',
         CategoryBlogView.as_view(), name='category_blog'),
    path('tag/<str:tag_slug>/', TagBlogView.as_view(), name='tag_blog'),
    path('search/', SearchPostView.as_view(), name='search_post'),
    path('markdownx/', include('markdownx.urls')),
    path('about/', about, name='about')
]
from django.urls import path
from blogs.views import index, detail, CategoryListView, TagListView, TagBlogView, CategoryBlogView

app_name = 'blogs'

urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:blog_id>/', detail, name='detail'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('tags/', TagListView.as_view(), name='tag_list'),
    path('category/<str:category_slug>/',
         CategoryBlogView.as_view(), name='category_blog'),
    path('tag/<str:tag_slug>/', TagBlogView.as_view(), name='tag_blog'),
]
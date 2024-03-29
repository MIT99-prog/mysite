from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.db.models import Count, Q
from .models import Blog, Category, Tag

def index(request):
    blogs = Blog.objects.filter(is_public__exact=True).order_by('-note_date')
    return render(request, 'blogs/index.html', {'blogs': blogs})

def detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    return render(request, 'blogs/detail.html', {'blog': blog})

def about(request):
    return render(request, 'blogs/about.html')

class IndexView(ListView):
    queryset = Blog.objects.filter(is_public__exact=True).order_by('-note_date')
    template_name = 'blogs/index.html'
    paginate_by = 10

class CategoryListView(ListView):
    queryset = Category.objects.annotate(
        num_posts=Count('blog', filter=Q(blog__is_public=True))
        )  # 下書き含まない件数
    # queryset = Category.objects.annotate(num_posts=Count('blog'))  # 下書き含む件数

class TagListView(ListView):
    queryset = Tag.objects.annotate(
        num_posts=Count('blog', filter=Q(blog__is_public=True))
        )  # 下書き含まない件数
    # queryset = Tag.objects.annotate(num_posts=Count('blog'))  # 下書き含む件数

class CategoryBlogView(ListView):
    model = Blog
    template_name = 'blogs/category_blog.html'

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        self.category = get_object_or_404(Category, slug=category_slug)
        lookups = (
            Q(category=self.category) &
            Q(is_public=True)
        )
        # qs = super().get_queryset().filter(category=self.category).order_by('-note_date')
        qs = super().get_queryset().filter(lookups).order_by('-note_date')
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context


class TagBlogView(ListView):
    model = Blog
    template_name = 'blogs/tag_blog.html'

    def get_queryset(self):
        tag_slug = self.kwargs['tag_slug']
        self.tag = get_object_or_404(Tag, slug=tag_slug)
        lookups = (
            Q(tags=self.tag) &
            Q(is_public=True)
        )
        # qs = super().get_queryset().filter(tags=self.tag).order_by('-note_date')
        qs = super().get_queryset().filter(lookups).order_by('-note_date')
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag
        return context

class SearchPostView(ListView):
    model = Blog
    template_name = 'blogs/search_blog.html'
    paginate_by = 10  # 表示件数

    def get_queryset(self):
        query = self.request.GET.get('q', None)
        lookups = (
            Q(title__icontains=query) |
            Q(text__icontains=query) |
            Q(category__name__icontains=query) |
            Q(tags__name__icontains=query)
        )
        if query is not None:
            qs = super().get_queryset().filter(lookups).distinct().order_by('-note_date')
            return qs
        qs = super().get_queryset()
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        return context

# For server error 500
from django.views.decorators.csrf import requires_csrf_token
from django.http import (
    HttpResponseBadRequest, HttpResponseForbidden, HttpResponseNotFound,
    HttpResponseServerError,)
@requires_csrf_token
def my_customized_server_error(request, template_name='500.html'):
    import sys
    from django.views import debug
    error_html = debug.technical_500_response(request, *sys.exc_info()).content
    return HttpResponseServerError(error_html)
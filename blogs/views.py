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

class IndexView(ListView):
    queryset = Blog.objects.filter(is_public__exact=True).order_by('-note_date')
    template_name = 'blogs/index.html'
    paginate_by = 10

class CategoryListView(ListView):
    queryset = Category.objects.annotate(
        num_posts=Count('blog', filter=Q(blog__is_public=True)))


class TagListView(ListView):
    queryset = Tag.objects.annotate(num_posts=Count(
        'blog', filter=Q(blog__is_public=True)))

class CategoryBlogView(ListView):
    model = Blog
    template_name = 'blogs/category_blog.html'

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        self.category = get_object_or_404(Category, slug=category_slug)
        qs = super().get_queryset().filter(category=self.category)
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
        qs = super().get_queryset().filter(tags=self.tag)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag
        return context

class SearchPostView(ListView):
    model = Blog
    template_name = 'blogs/search_blog.html'
    paginate_by = 3

    def get_queryset(self):
        query = self.request.GET.get('q', None)
        lookups = (
            Q(title__icontains=query) |
            Q(text__icontains=query) |
            Q(category__name__icontains=query) |
            Q(tags__name__icontains=query)
        )
        if query is not None:
            qs = super().get_queryset().filter(lookups).distinct()
            return qs
        qs = super().get_queryset()
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        return context
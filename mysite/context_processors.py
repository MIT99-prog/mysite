# dbsite/context_processors.py

from django.db.models import Count, Q

from blogs.models import Category, Tag


def common(request):
    context = {
        'categories': Category.objects.annotate(
            num_posts=Count('blog', filter=Q(blog__is_public=True))
            # 下書き含まない件数
            # num_posts=Count('blog')
            ),
        'tags': Tag.objects.annotate(
            num_posts=Count('blog', filter=Q(blog__is_public=True))
            # 下書き含まない件数
            # num_posts=Count('blog')
            ),
    }
    return context
from django.contrib import admin
# from markdownx.admin import MarkdownxModelAdmin

from blogs.models import Blog, Category, Tag

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'note_date', 'created_datetime', 'updated_datetime')
    list_display_links = ('id', 'title')

# admin.site.register(Blog, MarkdownxModelAdmin)    
admin.site.register(Blog, BlogAdmin)
# admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Tag)
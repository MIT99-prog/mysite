from django.db import models
from datetime import date
from django.utils import timezone

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)
    title = models.CharField(blank=False, null=False, max_length=150)
    text = models.TextField(blank=True)
    tag = models.CharField(blank=True, null=True, max_length=100)
    # temp = models.FileField(upload_to=user_directory_path)
    # file will be saved to MEDIA_ROOT/uploads/2015/01/30
    upload = models.FileField(blank=True, upload_to='uploads/%Y/%m/%d/')
    note_date =  models.DateField(default=date.today)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)
    is_public = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.is_public and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class ContentImage(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.PROTECT)
    content_image = models.FileField(upload_to='blogs_content_images/')

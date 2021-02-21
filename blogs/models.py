from django.db import models
from datetime import date

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Blog(models.Model):
    title = models.CharField(blank=False, null=False, max_length=150)
    text = models.TextField(blank=True)
    # temp = models.FileField(upload_to=user_directory_path)
    # file will be saved to MEDIA_ROOT/uploads/2015/01/30
    upload = models.FileField(blank=True, upload_to='uploads/%Y/%m/%d/')
    note_date =  models.DateField(default=date.today)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

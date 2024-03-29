# Generated by Django 2.1.15 on 2021-03-01 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0009_auto_20210301_0401'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_image', models.FileField(upload_to='blogs_content_images/')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blogs.Blog')),
            ],
        ),
    ]

# Generated by Django 2.1.15 on 2021-02-27 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_blog_note_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='tag',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

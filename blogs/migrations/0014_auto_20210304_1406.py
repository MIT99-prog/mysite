# Generated by Django 2.1.15 on 2021-03-04 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0013_auto_20210304_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='upload',
            field=models.FileField(blank=True, upload_to='media/%Y/%m/%d/'),
        ),
    ]

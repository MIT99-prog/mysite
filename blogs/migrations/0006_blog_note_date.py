# Generated by Django 2.1.15 on 2021-02-21 13:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_auto_20201209_0803'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='note_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]

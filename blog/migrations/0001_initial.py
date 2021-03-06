# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-04 20:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title_text', models.CharField(max_length=200)),
                ('article_content', models.TextField()),
                ('date_published', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import webapp.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(height_field='height_field', upload_to=webapp.models.upload_location, blank=True, null=True, width_field='width_field')),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=1500)),
                ('updated', models.TimeField(auto_now=True)),
                ('timestamp', models.TimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-id', '-timestamp', '-updated'],
            },
        ),
    ]

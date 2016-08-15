# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-04 08:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rear', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Content')),
                ('state', models.BooleanField(verbose_name='State')),
            ],
        ),
        migrations.DeleteModel(
            name='Text',
        ),
    ]
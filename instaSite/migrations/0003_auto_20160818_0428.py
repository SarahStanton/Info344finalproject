# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-18 04:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instaSite', '0002_auto_20160818_0401'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='picture',
            name='topic',
        ),
        migrations.AddField(
            model_name='picture',
            name='search',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='instaSite.Search'),
        ),
    ]

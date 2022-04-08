# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-12-20 06:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('boards', '0003_topic_views'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('details', models.CharField(max_length=100)),
                ('mrp', models.IntegerField()),
                ('discounted_price', models.IntegerField()),
                ('available', models.BooleanField(default=True)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='post',
            name='topic',
        ),
        migrations.RemoveField(
            model_name='post',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='board',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='starter',
        ),
        migrations.DeleteModel(
            name='Board',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
        migrations.AddField(
            model_name='product',
            name='product_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='boards.ProductCategory'),
        ),
        migrations.AddField(
            model_name='order',
            name='product_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='boards.ProductCategory'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_order', to=settings.AUTH_USER_MODEL),
        ),
    ]
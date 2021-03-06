# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-03-08 16:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0012_auto_20220308_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='product_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order', to='boards.Product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_user', to=settings.AUTH_USER_MODEL),
        ),
    ]

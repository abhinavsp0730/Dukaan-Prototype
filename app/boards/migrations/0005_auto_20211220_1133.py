# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-12-20 11:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0004_auto_20211220_0620'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_category',
        ),
        migrations.AlterField(
            model_name='order',
            name='product_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='boards.Product'),
        ),
        migrations.DeleteModel(
            name='ProductCategory',
        ),
    ]

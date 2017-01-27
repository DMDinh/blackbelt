# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-27 18:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register_app', '0004_auto_20170127_1808'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='register_app.Quote')),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='confirm_password',
        ),
        migrations.RemoveField(
            model_name='user',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='user',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='register_app.User'),
        ),
    ]
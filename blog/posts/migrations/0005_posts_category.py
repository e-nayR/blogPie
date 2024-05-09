# Generated by Django 5.0.4 on 2024-05-06 17:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('posts', '0004_alter_posts_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='categories.categories'),
        ),
    ]

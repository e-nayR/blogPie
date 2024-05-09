# Generated by Django 5.0.4 on 2024-05-08 18:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_categories_creator'),
        ('posts', '0008_alter_posts_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='categories.categories'),
        ),
    ]

# Generated by Django 5.0.4 on 2024-05-06 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categories',
            old_name='name',
            new_name='title',
        ),
    ]

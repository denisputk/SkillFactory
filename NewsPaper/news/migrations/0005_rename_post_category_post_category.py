# Generated by Django 4.1.3 on 2022-12-22 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_rename_category_category_category_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_category',
            new_name='category',
        ),
    ]

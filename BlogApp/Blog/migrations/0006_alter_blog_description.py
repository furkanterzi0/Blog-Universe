# Generated by Django 5.0.2 on 2024-02-29 09:20

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_blog_full_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]

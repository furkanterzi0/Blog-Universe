# Generated by Django 5.0.2 on 2024-02-29 09:22

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0006_alter_blog_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='full_description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]

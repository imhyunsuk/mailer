# Generated by Django 2.2.4 on 2019-09-10 05:09

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0002_auto_20190812_1406'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marketing',
            name='message',
        ),
        migrations.AddField(
            model_name='marketing',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
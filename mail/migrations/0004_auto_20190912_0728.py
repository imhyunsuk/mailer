# Generated by Django 2.2.4 on 2019-09-12 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0003_auto_20190910_0509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marketing',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]

# Generated by Django 3.1.5 on 2021-01-25 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0003_auto_20210125_1402'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='stock_type',
        ),
    ]

# Generated by Django 3.1.5 on 2021-01-25 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0002_stock_stock_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='stock_id',
            new_name='stock_code',
        ),
    ]

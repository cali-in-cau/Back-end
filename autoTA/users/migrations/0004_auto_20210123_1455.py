# Generated by Django 3.1.5 on 2021-01-23 05:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0001_initial'),
        ('users', '0003_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='stock',
            field=models.ForeignKey(db_column='stock_id', on_delete=django.db.models.deletion.CASCADE, related_name='f_stock', to='stocks.stock'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, related_name='f_user', to=settings.AUTH_USER_MODEL),
        ),
    ]

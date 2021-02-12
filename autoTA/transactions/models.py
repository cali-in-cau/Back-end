from django.db import models

# Create your models here.
class Transaction(models.Model):
    user = models.ForeignKey('users.User',related_name='t_user',on_delete=models.CASCADE,db_column='user_id')
    stock = models.ForeignKey('stocks.Stock',related_name='t_stock',on_delete=models.CASCADE,db_column='stock_id')
    trans_type = models.IntegerField(default=0, blank=False)
    trans_date = models.DateTimeField(auto_now=True)
    stock_price = models.IntegerField(default=0, blank=False)
    amount = models.IntegerField(default=0, blank=False)
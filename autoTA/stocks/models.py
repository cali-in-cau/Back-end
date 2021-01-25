from django.db import models

# Create your models here.
class Stock(models.Model):
    stock_type = models.CharField(max_length=100)
    stock_code = models.CharField(max_length=100)
    stock_name = models.CharField(max_length=100)

    def __str__(self):
        return self.stock_name

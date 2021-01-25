from django.db import models
from django.db.models import Q

keyword = request.GET.get('keyword','') #검색

# Create your models here.
class Stock(models.Model):
    stock_id = models.CharField(max_length=100)
    stock_name = models.CharField(max_length=100)

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.
class CustomAccountManager(BaseUserManager):

    def create_superuser(self,email,password, **other_fields):
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active',True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True')

        return self.create_user(email, **other_fields)
        
    def create_user(self,email, **other_fields):
        if not email:
            raise ValueError(_('You must provide an email'))

        email = self.normalize_email(email)
        user = self.model(email=email,  **other_fields)
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email'),unique=True)
    start_date = models.DateTimeField(default=timezone.now)
    account = models.CharField(max_length=100,blank=True)
    profit = models.IntegerField(default=0)
    asset = models.IntegerField(default=0)
    investment = models.IntegerField(default=0)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

class Favorite(models.Model):
    user = models.ForeignKey('User',related_name='f_user',on_delete=models.CASCADE,db_column='user_id')
    stock = models.ForeignKey('stocks.Stock',related_name='f_stock',on_delete=models.CASCADE,db_column='stock_id')
    



from email.mime import image
from django.db import models


# Create your models here.

class categry(models.Model):
    name=models.CharField(max_length=40)
    def __str__(self):
        return self.name
class Product(models.Model):
    name=models.CharField(max_length=40)
    price=models.IntegerField(default=0)
    cat=models.ForeignKey(categry, on_delete=models.CASCADE,default=1)
    description=models.CharField(max_length=200,default='')
    image=models.ImageField(upload_to='upload/products/')
    def __str__(self):
      return self.name 
    @staticmethod
    def get_all_products():
      return Product.objects.all()

    @staticmethod
    def get_all_products_by_categryid(categry_id):
      if categry_id:
       return Product.objects.filter(categry=categry_id)
      else:
        return Product.get_all_products();
class customber(models.Model):
  first_name=models.CharField(max_length=50)
  last_name=models.CharField(max_length=50)
  phone=models.CharField(max_length=15)
  email=models.EmailField()
  password=models.CharField(max_length=100)
  def __str__(self):
      return self.first_name
  def register(self):
    self.save()
  
  @staticmethod
  def get_customber_by_email():
    return customber.objects.filter(email_=_email)
  def isexists(self):
    if customber.objects.filter(email=self.email):
       return True
    else:
      return False
from django.db import models
import os
import datetime
# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=300)


class emp1(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
class company(models.Model):   
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    address=models.TextField(max_length=255)
def getFileName(requset,filename):
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename="%s%s"%(now_time,filename)
    return os.path.join('uploads/',new_filename)
class Product(models.Model):    
  name=models.CharField(max_length=150,null=False,blank=False)
  vendor=models.CharField(max_length=150,null=False,blank=False)
  product_image=models.ImageField(upload_to=getFileName,null=True,blank=True)
  quantity=models.IntegerField(null=False,blank=False)
  original_price=models.FloatField(null=False,blank=False)
  selling_price=models.FloatField(null=False,blank=False)
  description=models.TextField(max_length=500,null=False,blank=False)
  status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
  trending=models.BooleanField(default=False,help_text="0-default,1-Trending")
  created_at=models.DateTimeField(auto_now_add=True)
 
  def _str_(self) :
    return self.name 
 

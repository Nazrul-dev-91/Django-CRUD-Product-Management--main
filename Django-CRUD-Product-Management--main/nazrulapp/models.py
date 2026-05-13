from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    price =models.IntegerField()
    quantity = models.IntegerField()
    dis_per = models.IntegerField()
    tax = models.IntegerField()
    total = models.IntegerField()
    final_price = models.IntegerField()
    image = models.ImageField(upload_to='media/product_images/',null=True,blank=True)
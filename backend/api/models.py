from django.db import models


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    
class User_Number(models.Model):
    number=models.CharField(max_length=20,unique=True)
    country = models.ForeignKey(Country,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.number

class Category(models.Model):
    #country=models.ForeignKey(Country,on_delete=models.CASCADE,blank=False)
    country = models.ManyToManyField(Country)
    name = models.CharField(max_length=250)
    image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    

class Brand(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,blank=False)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    
class Coupon(models.Model):
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE,blank=False)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
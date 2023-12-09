from django.db import models


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=250)
    extension=models.CharField(max_length=6)


    def __str__(self):
        return self.name
    
class User_Number(models.Model):
    number=models.CharField(max_length=20,unique=True)
    country = models.ForeignKey(Country,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.number
    
    def extension(self):
        return self.country.extension

class Category(models.Model):
    #country=models.ForeignKey(Country,on_delete=models.CASCADE,blank=False)
    country = models.ManyToManyField(Country,blank=True,null=True)
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
    
    def countries(self):
        return ",".join([str(p) for p in self.country.all()])
    

class Brand(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,blank=False)
    name = models.CharField(max_length=250)
    image = models.ImageField(null=True,blank=True)
    country = models.ManyToManyField(Country,blank=True,null=True)
    topStore=models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
    def countries(self):
        return ",".join([str(p) for p in self.country.all()])
    
class Coupon(models.Model):
    description = models.CharField(max_length=250)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE,blank=False,related_name="coupons")
    code = models.CharField(max_length=250)
    

    def __str__(self):
        return self.description
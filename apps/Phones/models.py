from django.db import models

# Create your models here.

class MobileBrands(models.Model):
    brand_name = models.CharField("Brand",max_length=30,null=True,blank=True)
    class Meta: 
        verbose_name = "Mobile Brand"
        verbose_name_plural = "Mobile Brands"

class MobilePhone(models.Model):
    brand = models.ForeignKey(MobileBrands,on_delete=models.CASCADE)
    phone_name = models.CharField("Phone Name",max_length=30,null=True,blank=True)

    class Meta: 
        verbose_name = "Mobile Phone"
        verbose_name_plural = "Mobile Phones"
    
    
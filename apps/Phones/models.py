from django.db import models

# Create your models here.

class TimeStampedModel(models.Model):
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class MobileBrands(TimeStampedModel):
    brand_logo = models.FileField(upload_to="uploads",null=True,blank=True)
    brand_name = models.CharField("Brand",max_length=30,null=True,blank=True)
    class Meta: 
        verbose_name = "Mobile Brand"
        verbose_name_plural = "Mobile Brands"

    def __str__(self):
         return self.brand_name
    
class MobileSeries(TimeStampedModel):
    brand = models.ForeignKey(MobileBrands,on_delete=models.CASCADE)
    series_name = models.CharField("Series Name",max_length=30,null=True,blank=True)
    class Meta: 
        verbose_name = "Mobile Series"
        verbose_name_plural = "Mobile Series"

    def __str__(self):
         return self.series_name

class MobilePhone(TimeStampedModel):
    brand = models.ForeignKey(MobileBrands,on_delete=models.CASCADE)
    series = models.ForeignKey(MobileSeries,on_delete=models.CASCADE, null=True,blank=True)
    phone_name = models.CharField("Phone Name",max_length=30,null=True,blank=True)
    specs = models.JSONField("Phone specs")

    class Meta: 
        verbose_name = "Mobile Phone"
        verbose_name_plural = "Mobile Phones"
    
    
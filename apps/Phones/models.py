from django.db import models

from Tech_Web.apps.Phones.constant import BRAND_CHOICE


# Create your models here.

class MobilePhone(models.Model):
    phone_name = models.CharField("Phone Name",max_length=30,null=True,blank=True)
    brand = models.CharField("Phone Brand",max_length=30,choices=BRAND_CHOICE,null=True,blank=True)
    
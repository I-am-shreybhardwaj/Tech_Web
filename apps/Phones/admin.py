from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from apps.Phones.models import MobileBrands, MobilePhone, MobileSeries

# Register your models here.
@admin.register(MobileBrands)
class MobileBrandsAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','brand_name']
   
@admin.register(MobileSeries)
class MobileSeriesAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','brand','series_name']

@admin.register(MobilePhone)
class MobileBrandsAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','brand','phone_name']

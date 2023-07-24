from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from apps.Phones.models import MobileBrands

# Register your models here.
@admin.register(MobileBrands)
class MobileBrandsAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','brand_name']


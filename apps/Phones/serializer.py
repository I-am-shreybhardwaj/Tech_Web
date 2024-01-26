from rest_framework import serializers

from apps.Phones.models import MobilePhone, MobileBrands, MobileSeries

class BrandInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileBrands
        fields = ['id','brand_logo','brand_name']

class SeriesInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileSeries
        fields = ['id','series_name']

class MobileInfo(serializers.ModelSerializer):
    brand_name = serializers.SerializerMethodField()
    class Meta:
        model = MobilePhone
        fields = ['id','brand_name','phone_name','specs']

    def get_brand_name(self, obj):
        if obj and obj.brand:
            return obj.brand.brand_name
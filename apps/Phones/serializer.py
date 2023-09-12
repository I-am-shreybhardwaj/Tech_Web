from rest_framework import serializers

from apps.Phones.models import MobilePhone, MobileBrands

class BrandInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileBrands
        fields = "_all_"

class MobileInfo(serializers.ModelSerializer):
    class Meta:
        model = MobilePhone
        fields = ['brand','phone_name','specs']
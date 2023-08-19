from rest_framework import serializers

from apps.Phones.models import MobilePhone

class MobileInfo(serializers.ModelSerializer):
    class Meta:
        model = MobilePhone
        fields = ['brand','phone_name','specs']
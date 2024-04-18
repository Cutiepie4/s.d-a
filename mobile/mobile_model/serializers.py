from rest_framework import serializers
from .models import MobileCategory, Mobile

class MobileCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileCategory
        fields = ['category_name']

class MobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobile
        fields = '__all__'
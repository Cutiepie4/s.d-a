from rest_framework import serializers
from .models import ClothesCategory, Clothes

class ClothesCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothesCategory
        fields = ['category_name']

class ClothesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothes
        fields = '__all__'
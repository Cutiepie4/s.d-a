from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from djongo.models import Q
from .models import Clothes, ClothesCategory
from .serializers import ClothesSerializer, ClothesCategorySerializer

class ClothesViewSet(viewsets.ModelViewSet):
    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializer
    @action(detail=False, methods=['get'], url_path='search/(?P<keyword>[^/.]+)')
    def search(self, request, keyword=''):
        words = keyword.split()
        clothess = Clothes.objects.filter(
            Q(name__icontains=words[0]) | 
            Q(brand__icontains=words[0]) | 
            Q(meta_keyword__icontains=words[0])
        )
        serializer = ClothesSerializer(clothess, many=True)
        return Response(serializer.data)

class ClothesCategoryViewSet(viewsets.ModelViewSet):
    queryset = ClothesCategory.objects.all()
    serializer_class = ClothesCategorySerializer
from django.contrib import admin
from django.urls import path
from search_api.views import SearchAPIView

urlpatterns = [
    path('search/', SearchAPIView.as_view(), name='search'),
    path('search/<str:keyword>', SearchAPIView.as_view(), name='search_with_keyword'),
]

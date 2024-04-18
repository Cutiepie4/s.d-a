from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from cart_model.views import CartViewSet

router = DefaultRouter()
router.register(r'cart', CartViewSet)
urlpatterns = [
    path('', include(router.urls)),
]

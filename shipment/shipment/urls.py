from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from shipment_model.views import ShipmentStatusViewSet, ShipmentViewSet

router = DefaultRouter()
router.register(r'shipments', ShipmentViewSet)
router.register(r'shipment_status', ShipmentStatusViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from rest_framework import serializers
from .models import ShipmentStatus, Shipment

class ShipmentStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShipmentStatus
        fields = '__all__'

class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = '__all__'
        
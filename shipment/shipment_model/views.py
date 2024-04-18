from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Shipment, ShipmentStatus
from .serializers import ShipmentSerializer, ShipmentStatusSerializer

class ShipmentViewSet(viewsets.ModelViewSet):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
    
    def list(self, request, *args, **kwargs):
        shipments = self.get_queryset()
        serializer = self.get_serializer(shipments, many=True)
        data = serializer.data
        for item in data:
            shipment_status_id = item.get('shipment_status_id')
            if shipment_status_id:
                try:
                    shipment_status = ShipmentStatus.objects.get(status_id=shipment_status_id)
                    shipment_status_serializer = ShipmentStatusSerializer(shipment_status)
                    shipment_data['shipment_status'] = shipment_status_serializer.data
                except ShipmentStatus.DoesNotExist:
                    shipment_data['shipment_status'] = None

        return Response(data)

class ShipmentStatusViewSet(viewsets.ModelViewSet):
    queryset = ShipmentStatus.objects.all()
    serializer_class = ShipmentStatusSerializer
    
    def get_product_info(self, product_id):
        product_id_num = product_id.split('_')[1]
        service = None
        if 'book' in product_id:
            service = 'books'
        elif 'clothes' in product_id:
            service = 'clothes'
        elif 'mobile' in product_id:
            service = 'mobiles'

        if service:
            port_map = {'books': 8001, 'clothes': 8002, 'mobiles': 8003}
            port = port_map.get(service)
            if port:
                url = f"http://localhost:{port}/{service}/{product_id_num}"
                try:
                    response = requests.get(url)
                    if response.status_code == 200:
                        return response.json()
                except requests.RequestException as e:
                    pass
        return None

    @action(detail=False, methods=['get'], url_path='shipment_by_user/(?P<user_id>[^/.]+)')
    def shipment_by_user(self, request, user_id):
        shipment = Shipment.objects.filter(user_id=user_id)
        serializer = ShipmentSerializer(shipment, many=True)
        return Response(serializer.data)
            
        
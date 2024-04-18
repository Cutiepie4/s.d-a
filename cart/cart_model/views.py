from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from djongo.models import Q
from .models import Cart
from .serializers import CartSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serialized_data = []
        for item in queryset:
            product_id = item.product_id
            product_info = self.get_product_info(product_id)
            if product_info:
                item_data = CartSerializer(item).databases
                item_data['product'] = product_info
                serialized_data.append(item_data)
            
        return Response(serialized_data)
    
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

    @action(detail=False, methods=['get'], url_path='cart_by_user/(?P<user_id>[^/.]+)')
    def cart_by_user(self, request, user_id):
        cart = Cart.objects.filter(user_id=user_id)
        serializer = CartSerializer(cart, many=True)
        return Response(serializer.data)
            
        
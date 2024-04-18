from django.shortcuts import render
import requests
from rest_framework.views import APIView
from rest_framework.response import Response

class SearchAPIView(APIView):
    def get(self, request):
        query = request.query_params.get('query')
        if query:
            book_results = requests.get(f'http://localhost:8001/books/search/{query}'.json())
            clothes_results = requests.get(f'http://localhost:8001/clothes/search/{query}'.json())
            mobile_results = requests.get(f'http://localhost:8001/mobiles/search/{query}'.json())
        else:
            book_results = requests.get(f'http://localhost:8001/books/'.json())
            clothes_results = requests.get(f'http://localhost:8001/clothes/'.json())
            mobile_results = requests.get(f'http://localhost:8001/mobiles/'.json())

        return Response({
            'books': book_results,
            'clothes': clothes_results,
            'mobiles': mobile_results
        })
            
from django import views
from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.decorators import api_view

from .serializers import ProductSerializer
from .models import Product

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/product-list/',
        'Detail View': '/product-detail/<int:id>',
        'Create': '/product-create/',
        'Update': '/product-detail/<int:id>',
        'DElete': '/product-detail/<int:id>',
    }
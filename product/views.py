from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from Django.permissions import IsAdminOrIsAuthenticatedReadOnly
from product.serializers import ProductSerializer
from product.models import Product as ProductModel

from datetime import datetime
from django.db.models import Q


class ProductView(APIView):
    # 상품 조회
    def get(self, request):
        today = datetime.now()
        products = ProductModel.objects.filter(
            Q(exposure_start_date__lte=today, exposure_end_date__gte=today, ) | 
            Q(user=request.user)
        )
        serialized_data = ProductSerializer(products, many=True).data
        return Response(serialized_data, status=status.HTTP_200_OK)
    
    
    
    # 상품 등록
    def post(self, request):
        request.data['user'] = request.user.id
        product_serializer = ProductSerializer(data=request.data)
        
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    # 상품 수정
    def put(self, request, product_id):
        product = ProductModel.objects.get(id=product_id)
        product_serializer = ProductSerializer(product, data=request.data, partial=True)
        
        if product_serializer.is_valid():
            product_serializer.delete()
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        pass
    
        
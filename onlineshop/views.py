from django.shortcuts import render
from .models import Product, Order, Category
from .serializer import OrderSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

class OrderView(APIView):
    def get(self, request):
        try:
            orders = Order.objects.all()
            serializer = OrderSerializer(orders, many=True)
            return Response({
               'data': serializer.data,
               'message': 'Orders data fetched successfully'
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
               return Response({
               'data': {},
               'message': 'Something went wrong while fetching orders data'
            }, status=status.HTTP_400_BAD_REQUEST)

        
    def post(self, request):
         try:
            data = request.data
            serializer = OrderSerializer(data=data)
            if not serializer.is_valid():
                return Response({
               'data': {},
               'message': 'Something went wrong while fetching orders data'
            }, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response({
               'data': serializer.data,
               'message': 'Orders created successfully'
            }, status=status.HTTP_201_CREATED)
         
         except Exception as e:
            return Response({
               'data': {},
             'message': 'Something went wrong while creating orders'
            }, status=status.HTTP_400_BAD_REQUEST)
         
    def patch(self, request):
       try:
           data = request.data
           order = Order.objects.filter(id = data.get('id'))
           if not order.exists:
               return Response({
               'data': {},
               'message': 'Order is not found with this id'
            }, status=status.HTTP_400_BAD_REQUEST)
         
           serializer = OrderSerializer(order[0], data=data, partial=True)
          
           if not serializer.is_valid():
                return Response({
               'data': {},
               'message': 'Something went wrong'
            }, status=status.HTTP_500_BAD_REQUEST)
           serializer.save()
           
           return Response({
               'data': serializer.data,
               'message': 'Order is updated successfully'
            }, status=status.HTTP_200_OK)
         

       except:
           return Response({
               'data': {},
               'message': 'Something went wrong to create order'
            }, status=status.HTTP_400_BAD_REQUEST)
       
    def delete(self, request):
        try:
            data = request.data
            order = Order.objects.filter(id = data.get('id'))
            if not order.exists():
               return Response({
               'data': {},
               'message': 'Order is not found with this id'
            }, status=status.HTTP_400_BAD_REQUEST)
            order[0].delete()
            return Response({
               'data': {},
               'message': 'Order is deleted.'
            }, status=status.HTTP_200_OK)
         
        except:
            return Response({
               'data': {},
               'message': 'Something went wrong to deleting order'
            }, status=status.HTTP_400_BAD_REQUEST)
       
         
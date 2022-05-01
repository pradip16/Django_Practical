from rest_framework import status
from .serializers import ProductSerializers
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView
from .models import Product


class ListProductAPIView(ListAPIView):
    """This endpoint list all of the available Products from the database"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class CreateProductAPIView(CreateAPIView):
    """This endpoint allows for creation of a Product"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class UpdateProductAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific Product by passing in the id of the Product to update"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class DeleteProductAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Product from the database"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


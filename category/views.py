
from rest_framework import status
from .serializers import CategorySerializers
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView
from .models import Category

# Create your views here.
class ListCategoryAPIView(ListAPIView):
    """This endpoint list all of the available Categorys from the database"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

class CreateCategoryAPIView(CreateAPIView):
    """This endpoint allows for creation of a Category"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

class UpdateCategoryAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific Category by passing in the id of the Category to update"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

class DeleteCategoryAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Category from the database"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

from django.shortcuts import render
from category.models import Category
from product.models import Product

def index(request):
    c_data = Category.objects.latest('id')
    p_data = Product.objects.latest('id')
    return render(request,"index.html",{"c_data":c_data.pk,"p_data":p_data.pk})


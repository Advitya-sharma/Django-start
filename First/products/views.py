from django.shortcuts import render
from .models import Product
from .forms import ProductForm
# Create your views here.

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
        
    context = {'form':form}
    return render(request,"products/form.html",context)

def product_detail_view(request):   
    obj = Product.objects.get(id=5)
    context = {"object":obj}
    return render(request,"products/detail.html",context)

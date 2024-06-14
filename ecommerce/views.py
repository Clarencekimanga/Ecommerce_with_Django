from django.shortcuts import render
from .models import products

# Create your views here.
def product_list(request):
    products = product.object.all()
    context = {
        'products': products,
    }
    return render(request, 'htmlfile',context)
    
    def product_details(request):
        pass

import imp
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from store.models import Collection, Product, OrderItem
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def say_hello(request):
    queryset = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')
     
    return render( 
        request,
        'hello.html',
        {
            "name": "Ini",
            'products': list(queryset)
        }
    )
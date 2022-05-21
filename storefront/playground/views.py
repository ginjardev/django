from ast import Store
from select import select
from django.db import connection
from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Order, OrderItem, Collection

# Create your views here.
def say_hello(request):
    queryset = Product.objects.raw('select id, title FROM store_product')

    return render( 
        request,
        'hello.html',
        {
            "name": "Ini",
            'tags': list(queryset)
        }
    )
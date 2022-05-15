from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from django.db.models import Value
from store.models import Collection, Customer, Product, OrderItem, Order
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
# Create your views here.
def say_hello(request):
    queryset = Order.objects.select_related('customer').prefetch_related(
        'orderitem_set__product').order_by('-placed_at')[:5]
    result = Product.objects.filter(collection__id=3).aggregate(
        count=Count('id'), min_price=Min('unit_price'))
    query = Customer.objects.annotate(is_new=Value(True))
     
    return render( 
        request,
        'hello.html',
        {
            "name": "Ini",
            'results': list(query)
        }
    )
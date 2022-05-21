from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F, Func, ExpressionWrapper
from django.db.models import Value, DecimalField
from django.db.models.functions import Concat
from store.models import Collection, Customer, Product, OrderItem, Order
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.aggregates import Count, Max, Min, Avg, Sum


# Create your views here.
def say_hello(request):
    discounted_price = ExpressionWrapper(
        F('unit_price') * 0.8, output_field=DecimalField()
    )
    queryset = Order.objects.select_related('customer').prefetch_related(
        'orderitem_set__product').order_by('-placed_at')[:5]
    result = Product.objects.filter(collection__id=3).aggregate(
        count=Count('id'), min_price=Min('unit_price'))
    query = Customer.objects.annotate(
        full_name=Func(
            F('first_name'),
            Value(' '),
            F('last_name'),
            function='CONCAT'
        )
    )
    query2 = Customer.objects.annotate(
        full_name = Concat('first_name',Value(' '), 'last_name')
    )

    query3 = Product.objects.annotate(
        discounted_price = discounted_price
    )
     
    return render( 
        request,
        'hello.html',
        {
            "name": "Ini",
            'results': list(query3)
        }
    )
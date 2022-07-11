from dataclasses import fields
from rest_framework import serializers 
from store.models import *
from  decimal import Decimal 

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count'] 

    products_count = serializers.IntegerField(read_only=True)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
       model = Product
       fields = ['id', 'title', 'description', 'slug', 'inventory', 'unit_price', 'price_with_tax','collection']
    
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)
    


from _decimal import Decimal
from rest_framework import serializers

from store.models import Product, Collection


class CollectionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'slug', 'inventory', 'description', 'unit_price', 'price_with_tax', 'collection']
    #    we don't need to show slug,inventory and description but in order to save() in product_list
    #    to work we need these fields to add here

    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')


    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)

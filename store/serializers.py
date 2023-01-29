from _decimal import Decimal
from rest_framework import serializers

from store.models import Product, Collection


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=6, decimal_places=4, source='unit_price')
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    # this will get Collection model's string representation.
    # string representation of the Collection is its title[see Collection class in models.php],
    # therefore we get title of the associated collection of the product
    collection = serializers.StringRelatedField()


    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)

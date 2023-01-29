from _decimal import Decimal
from rest_framework import serializers

from store.models import Product


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    unit_price = serializers.DecimalField(max_digits=6, decimal_places=4)
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    def calculate_tax(self, product: Product):
        # this will throw an error, decimal cant multiply with float
        # return product.unit_price*1.1
        return product.unit_price * Decimal(1.1)

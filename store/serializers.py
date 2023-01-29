from _decimal import Decimal
from rest_framework import serializers

from store.models import Product, Collection


class CollectionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'unit_price', 'collection']

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)

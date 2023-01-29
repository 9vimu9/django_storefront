from rest_framework import serializers


# https://www.django-rest-framework.org/api-guide/serializers/

# serializer
# converts a model instance to a dictionary.
# model -> data internal representation
# serializer -> data outside representation

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    unit_price = serializers.DecimalField(max_digits=6, decimal_places=4)
    # serializer name has to be same as model attribute

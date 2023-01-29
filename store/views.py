from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from store.models import Product
from store.serializers import ProductSerializer


@api_view()
def product_list(request):
    return Response('ok')


@api_view()
def product_detail(request, id):
    try:
        product = Product.objects.get(pk=id)
        # get throws DoesNotExist exception if no model is to be found.
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

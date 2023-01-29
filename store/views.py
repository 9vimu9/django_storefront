from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from store.models import Product
from store.serializers import ProductSerializer


@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        queryset = Product.objects.select_related('collection').all()
        serializer = ProductSerializer(queryset, many=True, context={
            'request': request
        })
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():  # check input data are valid
            return Response('ok')
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            #  if input is invalid set status to 400 and returns errors like follow
            # {
            #     "title": [
            #         "This field is required."
            #     ],
            #     "unit_price": [
            #         "This field is required."
            #     ],
            #     "collection": [
            #         "This field is required."
            #     ]
            # }


@api_view()
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)


@api_view
def collection_detail(request, pk):
    return Response('ok')

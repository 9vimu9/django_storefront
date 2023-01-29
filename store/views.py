from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from store.models import Product
from store.serializers import ProductSerializer


@api_view(['GET', 'POST'])
# all the POST and GET requests come to
# /store/products will be redirected to the product_list
def product_list(request):
    if request.method == 'GET':
        queryset = Product.objects.select_related('collection').all()
        serializer = ProductSerializer(queryset, many=True, context={
            'request': request
        })
        return Response(serializer.data)

    if request.method == 'POST':
        # if the request is POST we can use the same serializer to convert
        # request using 'data' keyword
        serializer = ProductSerializer(data=request.data)
        return Response('ok')


@api_view()
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)


@api_view
def collection_detail(request, pk):
    return Response('ok')

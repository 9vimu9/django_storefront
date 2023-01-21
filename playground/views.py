from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from store.models import Product


def say_hello(request):
    # filter records that unit price is 20
    queryset = Product.objects.filter(unit_price=20)

    return render(request, 'hello.html', {'name': 'Vim', 'products': list(queryset)})

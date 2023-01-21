from django.shortcuts import render
from store.models import Product


def say_hello(request):
    # task : get products inventory less than 10 and price less than 20

    # using multiple params
    queryset = Product.objects.filter(inventory__lt=10, unit_price__lt=20)
    # using multiple filters
    queryset = Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20)

    return render(request, 'hello.html', {'name': 'Vim', 'products': list(queryset)})

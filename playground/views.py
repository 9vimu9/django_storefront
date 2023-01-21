from django.db.models import Q, F
from django.shortcuts import render
from store.models import Product


def say_hello(request):
    # ascending order by title
    queryset = Product.objects.order_by('title')

    # descending order by title
    queryset = Product.objects.order_by('-title')

    # sort with multiple columns
    # sorts smallest to the largest price, but when same price, it is sorted by title, but in descending order
    queryset = Product.objects.order_by('unit_price', '-title')

    # reverse the direction of sort
    queryset = queryset.reverse()

    # can be used after the filter
    queryset = Product.objects.filter(unit_price_gte=20).order_by('-unit_price')

    # sort and pick first result
    # --------------------------
    # slicing
    most_expensive_product = Product.objects.order_by('-unit_price')[0]
    # after slicing, it no longer returns queryset

    # earliest or latest
    chepest_product = Product.objects.earliest('unit_price')
    most_expensive_product = Product.objects.latest('unit_price')

    return render(request, 'hello.html', {'name': 'Vim', 'products': list(queryset)})

from django.db.models import Q, F
from django.shortcuts import render
from store.models import Product, OrderItem


def say_hello(request):
    # select_related can be used to connect 2 tables
    # with one-to-many relationship
    queryset = Product.objects.select_related('collection').all()

    # let's say collection has a relationship with a table, and
    # we need access to it.
    queryset = Product.objects.select_related('collection__someothertable').all()
    return render(request, 'hello.html', {'name': 'Vim', 'products': list(queryset)})

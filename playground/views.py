from django.db.models import Q, F
from django.shortcuts import render
from store.models import Product, OrderItem


def say_hello(request):

    # select_related => one-to-many
    # prefetch_related => many-to-many
    queryset = Product.objects.prefetch_related('promotions').all()

    # can add both in a single queryset
    queryset = Product.objects.\
        select_related('collection').\
        prefetch_related('promotions').all()

    return render(request, 'hello.html', {'name': 'Vim', 'products': list(queryset)})

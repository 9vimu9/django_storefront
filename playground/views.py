from django.db.models import Q, F
from django.shortcuts import render
from store.models import Product, OrderItem


def say_hello(request):
    # values => dict
    # values_list =>tuple
    # only => model instances
    # defer => model instances

    # ONLY
    # read marked columns only
    queryset = Product.objects.only('id', 'title')

    # DEFER
    # marked columns won't be added
    queryset = Product.objects.defer('description')
    return render(request, 'hello.html', {'name': 'Vim', 'products': list(queryset)})

from django.db.models import Q, F, Count, Min, Value, Func
from django.db.models.functions import Concat
from django.shortcuts import render
from store.models import Product, OrderItem, Order, Customer


def say_hello(request):
    queryset = Product.objects.annotate(
        discounted_price=F('unit_price')*0.8
    )
    # this will return following error
    # Cannot infer type of '*' expression involving these
    # types: DecimalField, FloatField. You must set output_field.
    return render(request, 'hello.html', {'name': 'Vim', 'products': list(queryset)})

from django.db.models import Q, F, Count, Min, Value, Func
from django.db.models.functions import Concat
from django.shortcuts import render
from store.models import Product, OrderItem, Order, Customer


def say_hello(request):
    # CONCAT using Func object
    queryset = Customer.objects.annotate(
        full_name=Func(F('first_name'), Value(' '), F('last_name'), function='CONCAT')
    )
    # SELECT `store_customer`.`id`,
    # ...
    # CONCAT(`store_customer`.`first_name`, ' ', `store_customer`.`last_name`) AS `full_name`
    # FROM `store_customer`

    # CONCAT using Concat object
    queryset = Customer.objects.annotate(
        full_name=Concat('first_name', Value(' '), 'last_name')
    )
    # more info about Django database functions
    # https://docs.djangoproject.com/en/4.1/ref/models/database-functions/

    return render(request, 'hello.html', {'name': 'Vim', 'products': list(queryset)})

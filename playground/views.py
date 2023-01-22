from django.db.models import Q, F, Count, Min, Value
from django.shortcuts import render
from store.models import Product, OrderItem, Order


def say_hello(request):
    # add columns temporarily
    queryset = Product.objects.annotate(temp_column=Value('12'))
    # SELECT `store_product`.`id`,
    # ...
    # '12' AS `temp_column`
    # FROM `store_product`

    queryset = Product.objects.annotate(new_title=F('title'))
    # SELECT `store_product`.`id`,
    # ...
    # `store_product`.`title` AS `new_title`
    # FROM `store_product`

    return render(request, 'hello.html', {'name': 'Vim', 'products': list(queryset)})

from django.db.models import Q, F, Count, Min, Value, Func, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from django.shortcuts import render
from store.models import Product, OrderItem, Order, Customer


def say_hello(request):
    discounted_price = ExpressionWrapper(
        F('unit_price') * 0.8, output_field=DecimalField()
    )
    # SELECT `store_product`.`id`,
    # ...
    # (`store_product`.`unit_price` * 0.8e0) AS `discounted_price`
    # FROM `store_product`
    queryset = Product.objects.annotate(
        discounted_price=discounted_price
    )
    return render(request, 'hello.html', {'name': 'Vim', 'products': list(queryset)})

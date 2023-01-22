from django.db.models import Q, F
from django.shortcuts import render
from store.models import Product, OrderItem, Order


def say_hello(request):
    # TASK
    # -----
    # get the last 5 orders with their customer and items, including products

    # step - 1
    # we want list of orders, therefore we should start with Order model.
    # first get last 5 orders
    queryset = Order.objects.order_by('-placed_at')[:5]

    # step - 2 get customers of those orders
    queryset = Order.objects.select_related('customer'). \
                   order_by('-placed_at')[:5]
    # single order can only have 1 customer only. therefore select_related is used.

    # step -3 preload items with the orders
    queryset = Order.objects.select_related('customer'). \
                   prefetch_related('orderitem_set'). \
                   order_by('-placed_at')[:5]
    # store_orderitem table has order_id column.
    # therefore we can get order detail from an order item.
    # vice versa, we should be able to get order items from an order as well.
    # In order to do that we can use 'orderitem_set'

    # single order can have multiple order items therefore prefetch_related is used

    # step - 4 load products referencing in OrderItem
    queryset = Order.objects.select_related('customer'). \
                   prefetch_related('orderitem_set__product'). \
                   order_by('-placed_at')[:5]

    return render(request, 'hello.html', {'name': 'Vim', 'products': list(queryset)})

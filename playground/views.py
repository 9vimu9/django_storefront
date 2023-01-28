from django.db.models import Q, F, Count, Min, Value, Func
from django.db.models.functions import Concat
from django.shortcuts import render
from store.models import Product, OrderItem, Order, Customer


def say_hello(request):
    # task :
    # add temporary column orders_count
    # store order count for that customer in orders_count column

    # Order model has customer Foreign Key
    # we can take customer of an order (order --> customer)
    # inversely we should be able to  get orders of a customer as well (customer --> Orders)
    # we can use `order_set` to do it

    # but here it doesn't work
    # order_set --> order

    # SELECT `store_customer`.`id`,
    # ...
    # COUNT(`store_order`.`id`) AS `orders_count`
    # FROM `store_customer`
    # LEFT OUTER JOIN `store_order`
    # ON (`store_customer`.`id` = `store_order`.`customer_id`)
    # GROUP BY `store_customer`.`id`
    # ORDER BY NULL

    queryset = Customer.objects.annotate(orders_count=Count('order'))
    return render(request, 'hello.html', {'name': 'Vim', 'products': list(queryset)})

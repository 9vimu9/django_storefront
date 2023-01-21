from django.db.models import Q, F
from django.shortcuts import render
from store.models import Product


def say_hello(request):
    # referencing columns
    # products that have equal inventory and price

    # this doesn't work
    # queryset = Product.objects.filter(inventory=unit_price)

    # using F objects
    queryset = Product.objects.filter(inventory=F('unit_price'))
    #     SELECT `store_product`.`id`,
    #     `store_product`.`title`,
    #     `store_product`.`slug`,
    #     `store_product`.`description`,
    #     `store_product`.`unit_price`,
    #     `store_product`.`inventory`,
    #     `store_product`.`last_update`,
    #     `store_product`.`collection_id`
    # FROM `store_product`
    # WHERE `store_product`.`inventory` = (`store_product`.`unit_price`)

    # F objects and referencing
    queryset = Product.objects.filter(inventory=F('collection__id'))
    #     SELECT `store_product`.`id`,
    #     `store_product`.`title`,
    #     `store_product`.`slug`,
    #     `store_product`.`description`,
    #     `store_product`.`unit_price`,
    #     `store_product`.`inventory`,
    #     `store_product`.`last_update`,
    #     `store_product`.`collection_id`
    # FROM `store_product`
    # WHERE `store_product`.`inventory` = (`store_product`.`collection_id`)

    return render(request, 'hello.html', {'name': 'Vim', 'products': list(queryset)})

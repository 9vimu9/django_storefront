from django.db.models import Q, F
from django.shortcuts import render
from store.models import Product, OrderItem


def say_hello(request):
    # values returns dictionary
    queryset = Product.objects.values('id', 'title')
    # SELECT `store_product`.`id`,
    # `store_product`.`title`
    # FROM `store_product`

    # get values from related columns
    # (one-to-many relationship is defined between Customer and Product models)
    queryset = Product.objects.values('title', 'collection__title')
    # SELECT `store_product`.`title`,
    # `store_collection`.`title`
    # FROM `store_product`
    # INNER JOIN `store_collection`
    # ON (`store_product`.`collection_id` = `store_collection`.`id`)

    # values == values_list
    # values returns dict
    # values_list returns tuple
    queryset = Product.objects.values_list('title')

    # QUESTION
    # ---------
    # select products that have been ordered and sort them by title
    queryset = OrderItem.objects.order_by('product__title').distinct().values('product__title')
    # but this returns array of dictionaries after the list. and we need array of products
    # for the html views. not OrderItem s
    queryset = Product.objects.filter(
        id__in=OrderItem.objects.distinct().values('product__id')
    ).order_by('title')
    # id__in === WHERE id IN

    # SELECT `store_product`.`id`,
    # `store_product`.`title`,
    # `store_product`.`slug`,
    # `store_product`.`description`,
    # `store_product`.`unit_price`,
    # `store_product`.`inventory`,
    # `store_product`.`last_update`,
    # `store_product`.`collection_id`
    # FROM `store_product`
    # WHERE `store_product`.`id` IN (
    #     SELECT DISTINCT U0.`product_id`
    # FROM `store_orderitem` U0
    # )
    # ORDER BY `store_product`.`title` ASC

    return render(request, 'hello.html', {'name': 'Vim', 'products': list(queryset)})

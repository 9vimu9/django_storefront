from django.db.models import Q, F
from django.shortcuts import render
from store.models import Product


def say_hello(request):
    # first 5 products
    # 0,1,2,3,4
    queryset = Product.objects.all()[:5]

    # next 5 products after the first 5
    # 5,6,7,8,9
    queryset = Product.objects.all()[5:10]
    #     SELECT `store_product`.`id`,
    #     `store_product`.`title`,
    #     `store_product`.`slug`,
    #     `store_product`.`description`,
    #     `store_product`.`unit_price`,
    #     `store_product`.`inventory`,
    #     `store_product`.`last_update`,
    #     `store_product`.`collection_id`
    # FROM `store_product`
    # LIMIT 5
    # OFFSET 5

    return render(request, 'hello.html', {'name': 'Vim', 'products': list(queryset)})

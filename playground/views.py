from django.shortcuts import render

from store.models import Product


def say_hello(request):
    # every model has attribute called 'objects' that can be  used to query the table
    query_set = Product.objects.all()
    # usually it returns query_set object.
    # not the actual result.

    # so we can use it to filter again and again and or to do further operations.
    query_set.filter().filter().order_by()

    # when it will be executed the query.

    # 1. when we loop a query set
    for product in query_set:
        print(product)
    # 2. converted to a list
    list(query_set)
    # 3. when we pick a specific item
    first_product = query_set[0]
    # 4. when we slice it.
    first_five_products = query_set[0:5]

    return render(request, 'hello.html', {'name': 'Vim'})

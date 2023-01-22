from django.db.models import Q, F, Count, Min
from django.shortcuts import render
from store.models import Product, OrderItem, Order


def say_hello(request):
    result = Product.objects. \
        aggregate(total_products=Count('id'))
    # {'total_products': 1000}

    result = Product.objects. \
        aggregate(total_products=Count('id'), minimum_price=Min('unit_price'))
    # {'total_products': 1000, 'minimum_price': Decimal('1.06')}

    # aggregate can be done on queryset
    result = Product.objects. \
        filter(collection__id=5). \
        aggregate(total_products=Count('id'), minimum_price=Min('unit_price'))
    # {'total_products': 245, 'minimum_price': Decimal('1.08')}

    return render(request, 'hello.html', {'name': 'Vim', 'products': list(queryset)})

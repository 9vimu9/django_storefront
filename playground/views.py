from django.contrib.contenttypes.models import ContentType
from django.db.models import Q, F, Count, Min, Value, Func, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from django.shortcuts import render
from store.models import Product, OrderItem, Order, Customer, Collection
from tags.models import TaggedItem


def say_hello(request):
    # method 1
    # ===========
    collection = Collection()
    collection.title = 'games'
    # assigning Product object to 'feature_product' field
    collection.featured_product = Product(pk=1)
    # or
    # directly assign value to the column
    collection.featured_product_id = 1
    collection.save()

    # method 2
    # ===========
    collection = Collection.objects.create(
        title='games',
        featured_product=Product(pk=1)
    )
    # INSERT INTO `store_collection` (`title`, `featured_product_id`)
    # VALUES ('games', 1)
    queryset = Product.objects.all()

    return render(request, 'hello.html', {'name': 'Vim', 'products': list(queryset)})

from django.contrib.contenttypes.models import ContentType
from django.db.models import Q, F, Count, Min, Value, Func, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from django.shortcuts import render
from store.models import Product, OrderItem, Order, Customer, Collection
from tags.models import TaggedItem


def say_hello(request):
    # method 1
    # ===========
    # get object from database that is wants to update
    collection = Collection.objects.get(pk=11)
    collection.title = 'games updated'
    # remove featured product
    collection.featured_product = None
    collection.save()

    # method 2
    # ===========
    Collection.objects.filter(pk=11).update(
        title='games',
    )
    # using this method, we can update multiple rows at once.

    # UPDATE `store_collection`
    # SET `title` = 'games'
    # WHERE `store_collection`.`id` = 11

    return render(request, 'hello.html', {'name': 'Vim', 'products': list(queryset)})

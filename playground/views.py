from django.contrib.contenttypes.models import ContentType
from django.db.models import Q, F, Count, Min, Value, Func, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from django.shortcuts import render
from store.models import Product, OrderItem, Order, Customer
from tags.models import TaggedItem


def say_hello(request):
    queryset = TaggedItem.objects.get_tags_for(Product, 1)
    return render(request, 'hello.html', {'name': 'Vim', 'products': list(queryset)})

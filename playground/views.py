from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from store.models import Product


def say_hello(request):
    # returns queryset with every record
    queryset = Product.objects.all()

    # returns the row that id is 1
    product = Product.objects.get(id=1)

    # returns the row that primary key column is 1
    # this is good, we don't need to know exact primary key name
    product = Product.objects.get(pk=1)

    # get throws exception if there is no record for the 'pk'
    try:
        Product.objects.get(pk=0)
    except ObjectDoesNotExist:
        pass

    # if you don't need exception to be thrown, then use 'filter'
    # returns none when there is no object.
    product = Product.objects.filter(pk=0).first()

    # check weather record is existed for the given conditions
    # returns bool
    is_product_exist = Product.objects.filter(pk=0).exists()

    return render(request, 'hello.html', {'name': 'Vim'})

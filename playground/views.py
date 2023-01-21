from django.shortcuts import render
from store.models import Product


def say_hello(request):
    # filter records that unit price is 20
    queryset = Product.objects.filter(unit_price=20)

    # unit price more than 20
    queryset = Product.objects.filter(unit_price__gt=20)

    # unit price equal or more than 20
    queryset = Product.objects.filter(unit_price__gte=20)

    # products unit price between 20 and 30
    queryset = Product.objects.filter(unit_price__range=(20, 30))

    # filter through one-to-many relationship
    queryset = Product.objects.filter(collection__title='Pets')

    queryset = Product.objects.filter(collection__id__range=(1, 3))

    # LIKE Lookups
    # case sensitive '%like%' query
    queryset = Product.objects.filter(title__contains='coffee')

    # case insensitive '%like%' query
    queryset = Product.objects.filter(title__icontains='coffee')

    # case sensitive 'like%' query
    queryset = Product.objects.filter(title__startswith='coffee')

    # case insensitive 'like%' query
    queryset = Product.objects.filter(title__istartswith='coffee')

    # DATE Lookups
    queryset = Product.objects.filter(last_update__year='2021')

    # NULL lookups
    # products without descriptions
    queryset = Product.objects.filter(description__isnull=True)

    # more field lookups
    # https://docs.djangoproject.com/en/4.1/ref/models/querysets/#field-lookups

    return render(request, 'hello.html', {'name': 'Vim', 'products': list(queryset)})

from django.db.models import Q, F
from django.shortcuts import render
from store.models import Product, OrderItem


def say_hello(request):
    queryset = Product.objects.all()
    return render(request, 'hello.html', {'name': 'Vim', 'products': list(queryset)})

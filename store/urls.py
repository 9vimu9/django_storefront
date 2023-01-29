from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('products/', views.product_list),
    path('products/<int:id>/', views.product_detail),  # throws 404 if id is not an int
    path('collections/<int:pk>/', views.collection_detail, name='collection-detail')  # throws 404 if id is not an int
]

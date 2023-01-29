from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('products/', views.product_list),
    path('products/<int:id>/', views.product_detail),
    path('collections/<int:pk>/', views.collection_detail, name='collection-detail')
    #    route name is used to connect with the hyperlink route field.
    #     int:pk is necessary cant use int:SOMETHING_ELSE
]

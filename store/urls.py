from rest_framework_nested import routers

from . import views

router = routers.SimpleRouter()  # SimpleRouter replaced by NestedSimpleRouter
router.register('products', views.ProductViewSet)
router.register('collections', views.CollectionViewSet)

# setup nested router
products_router = routers.NestedSimpleRouter(router, 'products', lookup='product_pk')
"""
router -> parent router
products -> pre-fix of the parent router that is used during parent router registration.
lookup='product_pk' -> The regex variable that matches an instance of the parent-resource
will be called '<lookup>_<parent-viewset.lookup_field>'
In the example above, lookup=domain and the parent viewset looks up
on 'pk' so the parent lookup regex will be 'domain_pk'.
Default: 'nested_<n>' where <n> is 1+parent_router.nest_count
"""
# register child route in the nested parent route
products_router.register('reviews', views.ReviewViewSet, basename='product-reviews')
"""
basename-> prefix that is used to generate URL patterns
so route names will be called product-reviews-detail, product-reviews-list .etc
"""
# http://localhost:8000/store/products/122/reviews/1/

# URLConf
urlpatterns = router.urls + products_router.urls

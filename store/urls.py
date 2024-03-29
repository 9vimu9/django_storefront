from rest_framework_nested import routers

from . import views

router = routers.SimpleRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet)
router.register('carts', views.CartViewSet)
products_router = routers.NestedSimpleRouter(router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet, basename='product-reviews')
carts_router = routers.NestedSimpleRouter(router, 'carts', lookup='cart')
carts_router.register('items', views.CartItemViewSet, basename='cart-items')
# URLConf
urlpatterns = router.urls + products_router.urls + carts_router.urls

from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register('products', views.ProductViewSet)  # SimpleRouter is used to create routes with ViewSet
router.register('collections', views.CollectionViewSet)

# URLConf
urlpatterns = router.urls  # urls attribute returns array of patterns of ViewSets.
# therefore we can directly assign it to urlpatterns

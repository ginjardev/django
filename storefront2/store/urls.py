from django.urls import path, include
from . import views  
from rest_framework.routers import SimpleRouter, DefaultRouter


router = DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('collections', views.CollectionViewSet)


#urlpatterns = router.urls

# URLConf
urlpatterns = [
    path('', include(router.urls))
]

 
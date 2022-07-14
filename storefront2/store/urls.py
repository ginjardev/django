from cgitb import lookup
from django.urls import path, include
from . import views  
from rest_framework.routers import SimpleRouter, DefaultRouter
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('collections', views.CollectionViewSet)

products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet, basename='product-reviews')
#urlpatterns = router.urls

# URLConf
# urlpatterns = [
#     path('', include(router.urls))
# ]

urlpatterns = router.urls + products_router.urls

 
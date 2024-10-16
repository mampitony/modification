from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EtablissementViewSet

router = DefaultRouter()

router.register('', EtablissementViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

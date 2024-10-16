from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import JoursFeriesViewSet

router = DefaultRouter()
router.register(r'jours-feries', JoursFeriesViewSet, basename='jours-feries')

urlpatterns = [
    path('', include(router.urls)),
]

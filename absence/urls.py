from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AbsenceViewSet, GestionCongesPayesViewSet

router = DefaultRouter()
router.register(r'abcences', AbsenceViewSet)
router.register(r'gestion-conges', GestionCongesPayesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

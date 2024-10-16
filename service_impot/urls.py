from django.urls import path
from .views import ServiceImpotEtablissementViewSet, ServiceImpotListView, ServiceImpotSocieteViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'societe', ServiceImpotSocieteViewSet)
router.register(r'etablissement', ServiceImpotEtablissementViewSet)


urlpatterns = [
    path('', ServiceImpotListView.as_view(), name='service-impot-list'),
    path('', include(router.urls)),
    # URL pour lister tous les établissements inscrits à un service d'impôt particulier
    path('<int:service_impot_id>/etablissements/', ServiceImpotEtablissementViewSet.as_view({'get': 'get_etablissements_par_service'}), name='etablissements-par-service'),
    # URL pour lister tous les services d'impôt d'un établissement particulier
    path('etablissement/<int:etablissement_id>/services/', ServiceImpotEtablissementViewSet.as_view({'get': 'get_services_par_etablissement'}), name='services-par-etablissement'),
]
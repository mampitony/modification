from django.urls import path, include
from .views import CentreDeCotisationListView, OrganismeSocialEtablissementViewSet, OrganismeSocialSocieteViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'societe', OrganismeSocialSocieteViewSet)
router.register(r'etablissement', OrganismeSocialEtablissementViewSet)

urlpatterns = [
    path('', CentreDeCotisationListView.as_view(), name='centre-de-cotisation-list'),
    path('', include(router.urls)),
    # Pas encore utiliser
    path('<int:organisme_social_id>/etablissements/', OrganismeSocialEtablissementViewSet.as_view({'get': 'get_etablissements_par_organisme_social'}), name='etablissement-par-organisme-social'),
    path('etablissement/<int:etablissement_id>/organismes/', OrganismeSocialEtablissementViewSet.as_view({'get': 'get_organisme_social_par_etablissement'}), name='organisme-social-par-etablissement')
]
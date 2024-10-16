# banque/urls.py
from django.urls import path
from .views import SocieteCreateUpdateView

urlpatterns = [
    # Autres URLs de l'application banque
    path('', SocieteCreateUpdateView.as_view(), name='societe-create-update'),
]

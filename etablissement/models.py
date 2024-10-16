from django.db import models

from banque.models import CompteBanque

# Create your models here.

class Etablissement(models.Model):
    nom_etablissement = models.CharField(max_length=255)
    adresse = models.CharField(max_length=511)
    activite = models.CharField(max_length=255)
    nom_responsable = models.CharField(max_length=255)
    prenoms_responsable = models.CharField(max_length=255)
    qualite_responsable = models.CharField(max_length=255)
    banque_1 = models.ForeignKey(CompteBanque, on_delete=models.CASCADE, related_name='etablisement_banque_1' )
    banque_2 = models.ForeignKey(CompteBanque, null=True, blank=True, on_delete=models.CASCADE, related_name='etablisement_banque_2')
    commentaire = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.nom_etablissement} ({self.adresse})"
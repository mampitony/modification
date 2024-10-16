from datetime import date
from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator
from banque.models import CompteBanque

# Create your models here.
class Societe(models.Model):
    raison_sociale = models.CharField(max_length = 255)
    nom_commercial = models.CharField(max_length = 255)
    adresse = models.CharField(max_length = 255)
    date_de_creation = models.DateField(default = date.today)
    forme_juridique = models.CharField(max_length = 255)
    numero_statistique = models.CharField(
        max_length = 255,
        validators=[RegexValidator(r'^\d+$', 'Le champ doit contenir que des chiffres.')],
    )
    numero_d_identite_fiscale = models.CharField(
        max_length = 10, 
        validators = [
            MinLengthValidator(10),
            MaxLengthValidator(10)
        ]
    )
    activite = models.CharField(max_length = 255)
    nom_responsable = models.CharField(max_length = 255)
    prenoms_responsable = models.CharField(max_length = 255)
    qualite_responsable = models.CharField(max_length = 255)
    banque_1 = models.ForeignKey(CompteBanque, on_delete = models.CASCADE, related_name = 'societe_banque_1' )
    banque_2 = models.ForeignKey(CompteBanque, on_delete = models.CASCADE, related_name = 'societe_banque_2')
    commentaire = models.TextField(null = True, blank = True)


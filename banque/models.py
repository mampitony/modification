from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Banque(models.Model):
    code_banque = models.CharField(max_length=3, unique=True)
    nom_banque = models.CharField(max_length=128)
    sigle_banque = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.code_banque}-{self.nom_banque}({self.sigle_banque})"
    
class CompteBanque(models.Model):
    banque = models.ForeignKey('Banque', on_delete=models.CASCADE)
    adresse_banque = models.CharField(max_length=255)
    iban = models.CharField(
        max_length=23,
        validators=[RegexValidator(r'^\d{23}$', 'Le champ doit contenir exactement 23 chiffres.')]
    )


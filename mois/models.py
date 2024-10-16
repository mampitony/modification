from django.db import models
from employe.models import Employe

# Create your models here.
class Mois(models.Model):
    annee = models.PositiveSmallIntegerField()
    mois = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 13)])
    
    def mois_annee(self):
        return f"{self.annee}-{self.mois}"

class MoisEmploye(models.Model):
    mois = models.ForeignKey(Mois, on_delete=models.CASCADE, related_name="mois_employe")
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE, related_name="employe_mois")
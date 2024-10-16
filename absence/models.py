from django.db import models
from employe.models import Employe
from mois.models import Mois

# Create your models here.
class Absence(models.Model):
    TYPE_D_ABSENCE = [
        ('Conges_payes','Congés payés'),
        ('Maladie','Maladie'),
        ('Justifie','Justifié'),
        ('Non_justifie', 'Non justifié')
    ]
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    debut_absence = models.DateField()
    fin_absence = models.DateField()
    type_d_absence = models.CharField(max_length=32, choices = TYPE_D_ABSENCE)
    nombre_d_heure_abcence = models.DecimalField(max_digits=3, decimal_places=3)

class GestionCongesPayes(models.Model):
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    mois = models.ForeignKey(Mois, on_delete=models.CASCADE)
    cp_acquis_du_mois = models.DecimalField(max_digits=5, decimal_places=3)
    cp_est_utilisable = models.BooleanField(default=True)

    @classmethod
    def conges_payes_cumules(self, employe):
        pass
    
    @classmethod
    def solde_conges_payes_cumule(self, employe):
        pass

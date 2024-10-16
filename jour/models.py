from django.db import models
from django.core.exceptions import ValidationError
from mois.models import MoisEmploye
from django.db.models import UniqueConstraint

# Create your models here.

class Jour(models.Model):
    date_jour = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 32)])
    mois = models.ForeignKey(MoisEmploye, on_delete=models.CASCADE, related_name='jour_travaille_employe')
    cantine_jours = models.PositiveSmallIntegerField(default=0)
    cantine_nuit = models.PositiveSmallIntegerField(default=0)
    transport_a_charge_societe = models.PositiveSmallIntegerField()
    transport_a_charge_employe = models.PositiveSmallIntegerField()

    class Meta:
        constraints = [
            UniqueConstraint(fields=['date_jour','mois'], name='date_jour_mois_unique')
        ]


class JoursFeries(models.Model):
    nom_jour_ferie = models.CharField(max_length=255)
    debut_jour_ferie = models.DateField()
    fin_jour_ferie = models.DateField()
    majoration_en_cas_de_travaille = models.DecimalField(max_digits=5, decimal_places=2, default=0, null=True, blank=True)

    def clean(self):
        if self.debut_jour_ferie < self.fin_jour_ferie:
            raise ValidationError('La date de fin jour férié doit être après la date de début jour férié.')
        
    def duree(self):
        return (self.fin_jour_ferie - self.debut_jour_ferie).days + 1
    
    def __str__(self) -> str:
        return f"{self.nom_jour_ferie} ({self.debut_jour_ferie} - {self.fin_jour_ferie}) : {self.duree()}"
    
    @staticmethod
    def verifier_jour_ferie(date):
        """Vérifie si la date est dans une période de jour férié."""
        jour_ferie = JoursFeries.objects.filter(debut_jour_ferie__lte=date, fin_jour_ferie__gte=date).first()
        if jour_ferie:
            return jour_ferie
        return None
    

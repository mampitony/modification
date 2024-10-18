from django.db import models
from etablissement.models import Etablissement

# Create your models here.

class ServiceImpot(models.Model):
    nom_service_impot = models.CharField(max_length=255)
    nom_de_l_impot = models.CharField(max_length=255)
    sigle_nom_de_l_impot = models.CharField(null=True, blank=True, max_length=255)


    def __str__(self):
        return f"{self.nom_service_impot}: {self.nom_de_l_impot}({self.sigle_nom_de_l_impot})"
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['nom_service_impot', 'nom_de_l_impot'], name='unique_nom_service_impot_nom_de_l_impot')
        ]

class ServiceImpotParent(models.Model):
    impot = models.ForeignKey(ServiceImpot, on_delete=models.CASCADE)
    adresse_service_impot = models.CharField(max_length=255)
    base_cotisation_imposable_employeur = models.DecimalField(max_digits=15, decimal_places=2)
    base_cotisation_imposable_salarie = models.DecimalField(max_digits=15, decimal_places=2)
    base_taux_impot_employeur = models.DecimalField(max_digits=15, decimal_places=2)
    base_taux_impot_salarie = models.DecimalField(max_digits=15, decimal_places=2)
    base_reduction_des_impots = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        abstract = True

class ServiceImpotSociete(ServiceImpotParent):
    
    def __str__(self) -> str:
        return (f"Impot: {self.impot.nom_de_l_impot} "
                f"Adresse: {self.adresse_service_impot} "
                f"Base cotisation imposable employeur: {self.base_cotisation_imposable_employeur} "
                f"Base cotisation imposable salarié: {self.base_cotisation_imposable_salarie} "
                f"Base taux impot employeur: {self.base_taux_impot_employeur} "
                f"Base taux impot salarié: {self.base_taux_impot_salarie} "
                f"Réduction des impôts: {self.base_reduction_des_impot}")

class ServiceImpotEtablissement(ServiceImpotParent):
    etablissement = models.ForeignKey(Etablissement, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return (f"Impot: {self.impot.nom_de_l_impot} "
                f"Etablissement: {self.etablissement.nom_etablissement} "
                f"Adresse: {self.adresse_service_impot} "
                f"Base cotisation imposable employeur: {self.base_cotisation_imposable_employeur} "
                f"Base cotisation imposable salarié: {self.base_cotisation_imposable_salarie} "
                f"Base taux impot employeur: {self.base_taux_impot_employeur} "
                f"Base taux impot salarié: {self.base_taux_impot_salarie} "
                f"Réduction des impôts: {self.base_reduction_des_impot}")

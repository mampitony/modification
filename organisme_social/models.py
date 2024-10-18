from django.db import models
from etablissement.models import Etablissement

# Create your models here.

# Modèle pour centre de cotisation
class CentreDeCotisation(models.Model):
    nom_organisme_social = models.CharField(unique=True, max_length=255)
    sigle = models.CharField(null=True, blank=True, max_length=255)

    def __str__(self):
        return f"{self.nom_organisme_social}({self.sigle})"

# Modèle parent abstrait pour les organismes sociaux
class OrganismeSocialParent(models.Model):
    organisme_social = models.ForeignKey(CentreDeCotisation, on_delete=models.CASCADE)
    adresse_organisme_social = models.CharField(max_length=255)
    base_cotisation_sociale_employeur = models.DecimalField(max_digits=15, decimal_places=2)
    base_cotisation_sociale_salarie = models.DecimalField(max_digits=15, decimal_places=2)
    base_taux_cotisation_sociale_employeur = models.DecimalField(max_digits=15, decimal_places=2)  # A demander si en pourcentage
    base_taux_cotisation_sociale_salarie = models.DecimalField(max_digits=15, decimal_places=2)    # A demander si en pourcentage

    class Meta:
        abstract = True

# Modèle dérivé pour la société
class OrganismeSocialSociete(OrganismeSocialParent):
    def __str__(self) -> str:
        return (f"Organisme social société: {self.organisme_social.nom_organisme_social} "
                f"Adresse: {self.adresse_organisme_social} "
                f"Base cotisation sociale employeur: {self.base_cotisation_sociale_employeur} "
                f"Base cotisation sociale salarié: {self.base_cotisation_sociale_salarie} "
                f"Taux cotisation sociale salarié: {self.base_taux_cotisation_sociale_salarie} "
                f"Taux cotisation sociale employeur: {self.base_taux_cotisation_sociale_employeur}")

# Modèle dérivé pour les établissements
class OrganismeSocialEtablissement(OrganismeSocialParent):
    etablissement = models.ForeignKey(Etablissement, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return (f"Organisme social établissement: {self.organisme_social.nom_organisme_social} "
                f"Etablissement: {self.etablissement} "
                f"Adresse: {self.adresse_organisme_social} "
                f"Base cotisation sociale employeur: {self.base_cotisation_sociale_employeur} "
                f"Base cotisation sociale salarié: {self.base_cotisation_sociale_salarie} "
                f"Taux cotisation sociale salarié: {self.base_taux_cotisation_sociale_salarie} "
                f"Taux cotisation sociale employeur: {self.base_taux_cotisation_sociale_employeur}")

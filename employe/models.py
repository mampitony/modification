from datetime import date
from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from etablissement.models import Etablissement
from dateutil.relativedelta import relativedelta

# Create your models here.

class Employe(models.Model):

    GENRE = [
        ('Homme', 'Homme'), 
        ('Femme', 'Femme')
    ]
    SITUATION_DE_FAMILLE = [
        ('Celibataire','Célibataire'),
        ('Marie','Marié'),
        ('Divorce','Divorcé'),
        ('Non_connue','Non connue')
    ]
    MOTIF_DE_SORTIE = [
        ('Demission', 'Démission'),
        ('Licenciement','Licenciement'),
        ('Fin_de_periode_d_essai_a_l_initiative_de_l_employeur','Fin de période d’essai à l’initiative de l’Employeur'),
        ('Fin_de_periode_d_essai_a_l_initiative_du_salarie','Fin de période d’essai à l’initiative du salarié'),
        ('Fin_du_CDD_par_l_employeur','Fin de CDD par l’Employeur'),
        ('Fin_du_CDD_par_le_salarie','Fin de CDD par le salarié')
    ]
    TYPE_DE_CONTRAT =[
        ('CDD','CDD'),
        ('CDI','CDI')
    ]
    MODE_DE_REGLEMENT = [
        ('Virement', 'Virement'),
        ('Cheque', 'Chèque')
    ]

    # Information personnelle
    nom = models.CharField(max_length = 255)
    prenoms = models.CharField(max_length = 255)
    genre = models.CharField(max_length = 10, choices = GENRE)
    date_de_naissance = models.DateField()
    lieu_de_naissance = models.CharField(max_length=512, default="Madagascar")
    nombre_d_enfant = models.IntegerField(default = 0)
    pays_de_naissance = models.CharField(max_length = 255)
    pays_de_nationnalite = models.CharField(max_length = 255)
    situation_de_famille = models.CharField(max_length = 32, choices = SITUATION_DE_FAMILLE)
    adresse = models.CharField(max_length = 255)
    numero_cin = models.CharField(
        max_length = 12,
        validators=[RegexValidator(r'^\d{12}$', 'Le champ doit contenir exactement 12 chiffres.')]
    )

    # Information proffessionnel

    matricule= models.CharField(max_length = 15, unique = True)
    email = models.EmailField(default='example@example.com')
    poste = models.CharField(max_length = 255)
    categorie_profesionnelle = models.CharField(max_length = 32)
    groupe = models.CharField(
        max_length = 1,
        validators=[RegexValidator(r'^\d{1}$', 'Le champ doit contenir exactement 1 chiffres.')]
    )
    date_d_embauche = models.DateField(default = date.today)
    date_de_sortie = models.DateField(default=None,null = True, blank = True)
    motif_de_sortie = models.CharField(max_length = 511, choices = MOTIF_DE_SORTIE, null = True, blank = True)
    type_de_contrat = models.CharField(max_length = 3, choices = TYPE_DE_CONTRAT, default = 'CDD')

    salaire_de_base = models.DecimalField(max_digits = 15, decimal_places = 2, default = 0.00)
    numero_cnaps = models.CharField(max_length = 32)
    mode_de_reglement = models.CharField(max_length = 16, choices = MODE_DE_REGLEMENT)
    numero_iban = models.CharField(
        max_length = 23,
        validators=[RegexValidator(r'^\d{23}$', 'Le champ doit contenir exactement 23 chiffres.')],
        null = True, blank = True
    )

    # Information de travaille
    
    heures_contractuelles = models.DecimalField(
        max_digits = 4, 
        decimal_places = 2, 
        default = 0.00,
        validators=[
            MinValueValidator(0), 
            MaxValueValidator(24)
        ]
    )
    travaille_lundi = models.BooleanField(default=True)
    travaille_mardi = models.BooleanField(default=True)
    travaille_mercredi = models.BooleanField(default=True)
    travaille_jeudi = models.BooleanField(default=True)
    travaille_vendredi = models.BooleanField(default=True)
    travaille_samedi = models.BooleanField(default=False)
    travaille_dimanche = models.BooleanField(default=False)

    est_en_travail_a_domicile = models.BooleanField(default = False)
    lieu_de_travaille = models.CharField(max_length = 128)
    affectation_ou_projet = models.CharField(max_length = 255)
    etablissement = models.ForeignKey(Etablissement, on_delete = models.SET_NULL, related_name = 'etablissement_employe', null= True)

    # Autres informations
    commentaire = models.TextField(blank = True, null = True)

    def anciennete_employe(self):
        if self.date_de_sortie:
            today = self.date_de_sortie
        else:
            today = date.today()
        years = today.year - self.date_d_embauche.year
        months = today.month - self.date_d_embauche.month
        days = today.day - self.date_d_embauche.day

        if days < 0:
            months -= 1
            days += (today.replace(month=today.month, day=1) - today.replace(month=today.month-1, day=1)).days

        if months < 0:
            years -= 1
            months += 12

        return {
            "annee": years,
            "mois": months,
            "jours": days
        }
    
    def heures_hebdomadaires(self):
        fois = 0
        if self.travaille_lundi:
            fois += 1
        if self.travaille_mardi:
            fois+=1
        if self.travaille_mercredi:
            fois+=1
        if self.travaille_jeudi:
            fois+=1
        if self.travaille_vendredi:
            fois+=1
        if self.travaille_samedi:
            fois+=1
        if self.travaille_dimanche:
            fois+=1

        return fois * self.heures_contractuelles
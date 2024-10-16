from django.db import models
from django.core.exceptions import ValidationError
from jour.models import Jour
# Create your models here.

class Action(models.Model):
    ACTION = [
        ('Travail', 'Travail'),
        ('Pause', 'Pause')
    ]
    jour = models.ForeignKey(Jour, on_delete=models.CASCADE, related_name='actions')
    heure_entre = models.TimeField()
    heure_sortie = models.TimeField()
    action = models.CharField(max_length=16, choices=ACTION)

    def clean(self) -> None:
        if self.heure_sortie <= self.heure_entre:
            raise ValidationError('L\'heure de sortie doit être après l\'heure d\'entrée.')

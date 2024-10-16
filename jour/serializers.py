from rest_framework import serializers
from action.serializers import ActionSerializer
from .models import Jour, JoursFeries

class JoursFeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = JoursFeries
        fields = [
            'pk', 
            'nom_jour_ferie', 
            'debut_jour_ferie', 
            'fin_jour_ferie', 
            'majoration_en_cas_de_travaille', 
            'duree'
        ]
        read_only_fields = ['duree']

class JourSerializer(serializers.ModelSerializer):
    actions = ActionSerializer(many=True)

    class Meta:
        model = Jour
        fields = [
            'date_jour', 
            'mois',
            'cantine_jours', 
            'cantine_nuit', 
            'transport_a_charge_societe', 
            'transport_a_charge_employe',
            'actions'
        ]
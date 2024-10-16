from rest_framework import serializers
from etablissement.serializers import EtablissementSerializer
from .models import Employe

class EmployeSerializer(serializers.ModelSerializer):
    etablissement_info = EtablissementSerializer(source='etablissement', read_only=True)
    anciennete = serializers.SerializerMethodField()
    heures_hebdomadaires = serializers.SerializerMethodField()

    class Meta:
        model = Employe
        fields = '__all__'

    def get_anciennete(self, obj):
        return obj.anciennete_employe()
    
    def get_heures_hebdomadaires(self, obj):
        return obj.heures_hebdomadaires()
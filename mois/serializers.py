from rest_framework import serializers
from mois.models import Mois, MoisEmploye
from employe.serializers import EmployeSerializer

class MoisSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mois
        fields = ['pk', 'annee', 'mois', 'mois_annee']
        read_only_fields = ['mois_annee']

class MoisEmployeSerializer(serializers.ModelSerializer):
    mois_info = MoisSerializer(source='mois', read_only = True)
    employe_info = EmployeSerializer(source= 'employe', read_only=True)

    class Meta:
        model = MoisEmploye
        fields = ['mois_info', 'employe_info']
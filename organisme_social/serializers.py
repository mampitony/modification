from rest_framework import serializers
from .models import CentreDeCotisation, OrganismeSocialEtablissement, OrganismeSocialSociete

class CentreDeCotisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentreDeCotisation
        fields = ['pk', 'nom_organisme_social','sigle']

class OrganismeSocialSocieteSerializer(serializers.ModelSerializer):
    organisme_social_info = CentreDeCotisationSerializer(source='organisme_social', read_only=True)

    class Meta:
        model = OrganismeSocialSociete
        fields = '__all__'

class OrganismeSocialEtablissementSerializer(serializers.ModelSerializer):
    organisme_social_info = CentreDeCotisationSerializer(source='organisme_social', read_only=True)
    class Meta:
        model = OrganismeSocialEtablissement
        fields = '__all__'

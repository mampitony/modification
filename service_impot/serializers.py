from rest_framework import serializers
from .models import ServiceImpot, ServiceImpotEtablissement, ServiceImpotSociete


class ServiceImpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceImpot
        fields = ['pk','nom_service_impot','nom_de_l_impot','sigle_nom_de_l_impot']

class ServiceImpotSocieteSerializer(serializers.ModelSerializer):
    service_impot_info = ServiceImpotSerializer(source='impot', read_only=True)

    class Meta:
        model = ServiceImpotSociete
        fields = '__all__'

class ServiceImpotEtablissementSerializer(serializers.ModelSerializer):
    service_impot_info = ServiceImpotSerializer(source='impot', read_only=True)

    class Meta:
        model = ServiceImpotEtablissement
        fields = '__all__'

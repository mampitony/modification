from rest_framework import serializers
from .models import Absence, GestionCongesPayes

class AbsenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Absence
        fields = '__all__'

class GestionCongesPayesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GestionCongesPayes
        fields = '__all__'

from rest_framework import serializers
from .models import Banque, CompteBanque

class BanqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banque
        fields = ['pk','code_banque', 'nom_banque', 'sigle_banque']
        
class CompteBanqueSerializer(serializers.ModelSerializer):
    banque_info = BanqueSerializer(source='banque', read_only=True)
    
    class Meta:
        model = CompteBanque
        fields = ['adresse_banque','iban','banque_info', 'banque']

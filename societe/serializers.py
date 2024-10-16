from rest_framework import serializers
from banque.serializers import CompteBanqueSerializer
from etablissement.models import Etablissement
from .models import Societe
from banque.models import CompteBanque

class SocieteSerializer(serializers.ModelSerializer):
    banque_1 = CompteBanqueSerializer()
    banque_2 = CompteBanqueSerializer()
    nombre_etablissement = serializers.SerializerMethodField(read_only = True)
    

    class Meta:
        model = Societe
        fields = '__all__'

    def create(self, validated_data):
        banque_1_data = validated_data.pop('banque_1')
        banque_2_data = validated_data.pop('banque_2')

        banque_1, _ = CompteBanque.objects.get_or_create(**banque_1_data)
        banque_2, _ = CompteBanque.objects.get_or_create(**banque_2_data)

        societe = Societe.objects.create(banque_1=banque_1, banque_2=banque_2, **validated_data)
        return societe
    
    def update(self, instance, validated_data):
        banque_1_data = validated_data.pop('banque_1', None)
        banque_2_data = validated_data.pop('banque_2', None)

        # Update banque_1 if data is provided
        if banque_1_data:
            # Si l'instance de banque_1 existe, on la met à jour
            if instance.banque_1:
                for attr, value in banque_1_data.items():
                    setattr(instance.banque_1, attr, value)
                instance.banque_1.save()  # Sauvegarde les modifications
            else:
                # Créer une nouvelle instance si elle n'existe pas
                instance.banque_1 = CompteBanque.objects.create(**banque_1_data)

        # Update banque_2 if data is provided
        if banque_2_data:
            # Si l'instance de banque_2 existe, on la met à jour
            if instance.banque_2:
                for attr, value in banque_2_data.items():
                    setattr(instance.banque_2, attr, value)
                instance.banque_2.save()  # Sauvegarde les modifications
            else:
                # Créer une nouvelle instance si elle n'existe pas
                instance.banque_2 = CompteBanque.objects.create(**banque_2_data)

        # Update other fields of the main instance
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance

    
    def get_nombre_etablissement(self, obj):

        return Etablissement.objects.count()
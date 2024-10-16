from rest_framework import serializers

from banque.models import CompteBanque
from banque.serializers import CompteBanqueSerializer
from .models import Etablissement

class EtablissementSerializer(serializers.ModelSerializer):
    banque_1 = CompteBanqueSerializer()
    banque_2 = CompteBanqueSerializer()

    class Meta:
        model = Etablissement
        fields = '__all__'

    def create(self, validated_data):
        banque_1_data = validated_data.pop('banque_1')
        banque_2_data = validated_data.pop('banque_2')

        banque_1, _ = CompteBanque.objects.get_or_create(**banque_1_data)
        banque_2, _ = CompteBanque.objects.get_or_create(**banque_2_data)

        etablissement = Etablissement.objects.create(banque_1=banque_1, banque_2=banque_2, **validated_data)
        return etablissement

    def update(self, instance, validated_data):
        banque_1_data = validated_data.pop('banque_1', None)
        banque_2_data = validated_data.pop('banque_2', None)

        if banque_1_data:
            if instance.banque_1:
                for attr, value in banque_1_data.items():
                    setattr(instance.banque_1, attr, value)
                instance.banque_1.save()
            else:
                instance.banque_1 = CompteBanque.objects.create(**banque_1_data)

        if banque_2_data:
            if instance.banque_2:
                for attr, value in banque_2_data.items():
                    setattr(instance.banque_2, attr, value)
                instance.banque_2.save() 
            else:
                instance.banque_2 = CompteBanque.objects.create(**banque_2_data)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

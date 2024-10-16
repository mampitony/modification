from rest_framework import serializers
from action.models import Action

class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = ['pk', 'jour', 'heure_entre', 'heure_sortie', 'action']
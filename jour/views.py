from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils.dateparse import parse_date
from django.core.exceptions import ValidationError
from datetime import date
from .models import JoursFeries
from .serializers import JoursFeriesSerializer
# Create your views here.

class JoursFeriesViewSet(viewsets.ModelViewSet):
    queryset = JoursFeries.objects.all().order_by('debut_jour_ferie')
    serializer_class = JoursFeriesSerializer

    # Récupérer les jours fériés d'une année spécifique
    @action(detail=False, methods=['get'], url_path='annee/(?P<annee>[0-9]{4})')
    def par_annee(self, request, annee=None):
        try:
            year = int(annee)
            jours_feries = JoursFeries.objects.filter(debut_jour_ferie__year=year)
            serializer = self.get_serializer(jours_feries, many=True)
            return Response(serializer.data)
        except ValueError:
            return Response({'detail': 'Année invalide.'}, status=status.HTTP_400_BAD_REQUEST)

    # Récupérer les jours fériés d'un mois spécifique
    @action(detail=False, methods=['get'], url_path='mois/(?P<annee>[0-9]{4})/(?P<mois>[0-9]{2})')
    def par_mois(self, request, annee=None, mois=None):
        try:
            year = int(annee)
            month = int(mois)
            jours_feries = JoursFeries.objects.filter(debut_jour_ferie__year=year, debut_jour_ferie__month=month)
            serializer = self.get_serializer(jours_feries, many=True)
            return Response(serializer.data)
        except ValueError:
            return Response({'detail': 'Année ou mois invalide.'}, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

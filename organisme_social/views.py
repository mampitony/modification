from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets, status
from rest_framework.response import Response

from etablissement.models import Etablissement
from etablissement.serializers import EtablissementSerializer

from .serializers import CentreDeCotisationSerializer, OrganismeSocialEtablissementSerializer, OrganismeSocialSocieteSerializer
from .models import CentreDeCotisation, OrganismeSocialEtablissement, OrganismeSocialSociete

# Create your views here.
class CentreDeCotisationListView(generics.ListAPIView):
    queryset = CentreDeCotisation.objects.all()
    serializer_class = CentreDeCotisationSerializer

class OrganismeSocialSocieteViewSet(viewsets.ModelViewSet):
    queryset = OrganismeSocialSociete.objects.all()
    serializer_class = OrganismeSocialSocieteSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        print("Liste")
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        print("Retrieve")
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("Create")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            print("Update")
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        print("Delete")
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrganismeSocialEtablissementViewSet(viewsets.ModelViewSet):
    queryset = OrganismeSocialEtablissement.objects.all()
    serializer_class = OrganismeSocialEtablissementSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        print("Liste")
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        print("Retrieve")
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("Create")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            print("Update")
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        print("Delete")
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def get_organisme_social_par_etablissement(self, request, etablissement_id=None):
        """Lister tous les organismes sociaux d'un établissement particulier."""
        organisme = self.queryset.filter(etablissement_id=etablissement_id)
        
        if not organisme.exists():
            return Response(
                []
            )
        
        serializer = self.serializer_class(organisme, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_etablissements_par_organisme_social(self, request, organisme_social_id=None):
        """Lister tous les établissements inscrits à un service impôt particulier."""
        etablissements = OrganismeSocialEtablissement.objects.filter(organisme_social_id=organisme_social_id)

        if not etablissements.exists():
            return Response(
                []
            )
        
        # Utiliser un serializer d'Etablissement pour obtenir les détails complets
        etablissements_ids = etablissements.values_list('etablissement', flat=True)
        etablissements_obj = Etablissement.objects.filter(id__in=etablissements_ids)
        etablissement_serializer = EtablissementSerializer(etablissements_obj, many=True)

        return Response(etablissement_serializer.data, status=status.HTTP_200_OK)
from etablissement.models import Etablissement
from etablissement.serializers import EtablissementSerializer
from service_impot.models import ServiceImpot, ServiceImpotEtablissement, ServiceImpotSociete
from rest_framework import generics
from .serializers import ServiceImpotEtablissementSerializer, ServiceImpotSerializer, ServiceImpotSocieteSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response

# Create your views here.
class ServiceImpotListView(generics.ListAPIView):
    queryset = ServiceImpot.objects.all()
    serializer_class = ServiceImpotSerializer

    
class ServiceImpotSocieteViewSet(viewsets.ModelViewSet):
    queryset = ServiceImpotSociete.objects.all()
    serializer_class = ServiceImpotSocieteSerializer
    
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

class ServiceImpotEtablissementViewSet(viewsets.ModelViewSet):
    queryset = ServiceImpotEtablissement.objects.all()
    serializer_class = ServiceImpotEtablissementSerializer

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
    
    def get_services_par_etablissement(self, request, etablissement_id=None):
        """Lister tous les services d'impôt d'un établissement particulier."""
        services = self.queryset.filter(etablissement_id=etablissement_id)
        
        if not services.exists():
            return Response(
                []
            )
        
        serializer = self.serializer_class(services, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_etablissements_par_service(self, request, service_impot_id=None):
        """Lister tous les établissements inscrits à un service d'impôt particulier."""
        services = ServiceImpotEtablissement.objects.filter(impot_id=service_impot_id)

        if not services.exists():
            return Response(
                []
            )
        
        # Récupérer les objets Etablissement associés
        etablissement_ids = services.values_list('etablissement', flat=True)
        etablissements = Etablissement.objects.filter(id__in=etablissement_ids)
        etablissement_serializer = EtablissementSerializer(etablissements, many=True)

        return Response(etablissement_serializer.data, status=status.HTTP_200_OK)
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Etablissement
from .serializers import EtablissementSerializer
from societe.models import Societe
# Create your views here.

class EtablissementViewSet(viewsets.ModelViewSet):
    queryset = Etablissement.objects.all().order_by('nom_etablissement')
    serializer_class = EtablissementSerializer
    lookup_field = 'pk'

    def dispatch(self, *args, **kwargs):
        # Vérifie si la société est initialisée
        try:
            Societe.objects.get(pk=1)
        except Societe.DoesNotExist:
            return Response({"detail": "La société doit être initialisée avant de pouvoir gérer les établissements."}, status=status.HTTP_400_BAD_REQUEST)
        return super().dispatch(*args, **kwargs)

    # Surcharge de la méthode 'list' (GET /etablissemnent/)
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        print("Liste")
        return Response(serializer.data)

    # Surcharge de la méthode 'retrieve' (GET /etablissemnent/{pk}/)
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        print("Retrieve")
        return Response(serializer.data)

    # Surcharge de la méthode 'create' (POST /etablissemnent/)
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("Create")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Surcharge de la méthode 'update' (PUT /etablissemnent/{pk}/)
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            print("Update")
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Surcharge de la méthode 'destroy' (DELETE /etablissemnent/{pk}/)
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        print("Delete")
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# societe/views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound, ValidationError
from .models import Societe
from .serializers import SocieteSerializer

class SocieteCreateUpdateView(generics.RetrieveUpdateAPIView, generics.CreateAPIView):
    queryset = Societe.objects.all()
    serializer_class = SocieteSerializer
    lookup_field = 'pk'

    def get_object(self):
        try:
            # Assurer que l'identifiant de la société est 1
            return Societe.objects.get(pk=1)
        except Societe.DoesNotExist:
            # Si la société n'existe pas, lever une exception NotFound
            raise NotFound("La société n'a pas encore été créée.")

    def post(self, request, *args, **kwargs):
        # Vérifiez si la société avec pk=1 existe déjà
        if Societe.objects.filter(pk=1).exists():
            raise ValidationError(detail="La société a déjà été initialisée.")
        
        # Créez une nouvelle société avec l'ID 1
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Assurez-vous que le pk est 1
            serializer.validated_data['id'] = 1
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        # Mettre à jour la société existante avec l'ID 1
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_success_headers(self, data):
        try:
            return {'Location': str(data.get('url'))}
        except (TypeError, AttributeError):
            return {}

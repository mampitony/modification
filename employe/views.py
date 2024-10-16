from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Employe
from .serializers import EmployeSerializer

class EmployeViewSet(viewsets.ModelViewSet):
    queryset = Employe.objects.all().order_by('matricule')
    serializer_class = EmployeSerializer
    lookup_field = 'pk'

    # Surcharge de la méthode 'list' (GET /employes/)
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        print("Liste")
        return Response(serializer.data)

    # Surcharge de la méthode 'retrieve' (GET /employes/{pk}/)
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        print("Retrieve")
        return Response(serializer.data)

    # Surcharge de la méthode 'create' (POST /employes/)
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("Create")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Surcharge de la méthode 'update' (PUT /employes/{pk}/)
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            print("Update")
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Surcharge de la méthode 'destroy' (DELETE /employes/{pk}/)
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        print("Delete")
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Banque
from .serializers import BanqueSerializer

class BanqueListView(generics.ListAPIView):
    queryset = Banque.objects.all()
    serializer_class = BanqueSerializer

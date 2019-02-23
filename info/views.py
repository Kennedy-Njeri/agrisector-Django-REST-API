from django.shortcuts import render
from rest_framework import generics
from .models import Info
from .serializers import InfoSerializer
from rest_framework import viewsets

# Create your views here.

class InfoViewSet(viewsets.ModelViewSet):
    """
    Provides a get method handler.
    """
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
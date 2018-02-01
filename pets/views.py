from rest_framework.generics import ListCreateAPIView
from django.shortcuts import render

from pets.models import Animal
from pets.serializers import AnimalSerializer


class AnimalListCreateView(ListCreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

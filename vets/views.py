from rest_framework.generics import ListCreateAPIView
from django.shortcuts import render

from vets.models import Vet
from vets.serializers import VetSerializer


class VetListCreateView(ListCreateAPIView):
    queryset = Vet.objects.all()
    serializer_class = VetSerializer

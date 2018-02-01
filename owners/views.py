from rest_framework.generics import ListCreateAPIView
from django.shortcuts import render

from owners.models import Owner
from owners.serializers import OwnerSerializer


class OwnerListCreateView(ListCreateAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

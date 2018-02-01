from rest_framework.generics import ListCreateAPIView
from django.shortcuts import render

from hospitals.models import Hospital
from hospitals.serializers import HospitalSerializer


class HospitalListCreateView(ListCreateAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer

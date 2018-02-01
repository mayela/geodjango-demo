from rest_framework import serializers
from rest_framework_gis.serializers import GeoModelSerializer, GeoFeatureModelSerializer

from vets.serializers import VetSerializer

from hospitals.models import Hospital


#class HospitalSerializer(serializers.ModelSerializer):
class HospitalSerializer(GeoFeatureModelSerializer):
    chief_vet = VetSerializer()
    class Meta:
        model = Hospital
        geo_field = "location"
        fields = ('chief_vet', 'name', 'address', 'license')

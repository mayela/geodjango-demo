from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from hospitals.models import Hospital


#class HospitalSerializer(serializers.ModelSerializer):
class HospitalSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Hospital
        geo_field = "location"
        fields = ('name', 'address', 'license')

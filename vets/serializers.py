from rest_framework import serializers

from owners.serializers import UserSerializer

from vets.models import Vet


class VetSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Vet
        fields = ('user', 'certification')

from rest_framework import serializers

from pets.models import Animal


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ('id', 'name', 'breed', 'age', 'sound', 'owner')

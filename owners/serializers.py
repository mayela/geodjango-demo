from django.contrib.auth.models import User

from rest_framework import serializers

from owners.models import Owner


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class OwnerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Owner
        fields = ('user', 'membership')

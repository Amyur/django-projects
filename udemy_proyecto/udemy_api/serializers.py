from rest_framework import serializers
from udemy_api.models import Paises

class PaisesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Paises
        fields = ("id", "name", "capital")
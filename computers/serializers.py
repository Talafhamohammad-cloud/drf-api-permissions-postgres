from rest_framework import serializers
from .models import Computers


class ComputersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computers
        fields = ('id', 'modelComputers', 'description', 'author')

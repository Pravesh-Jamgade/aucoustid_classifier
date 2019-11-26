from rest_framework import serializers
from boards.models import ServiceData

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceData
        fields = '__all__'

    
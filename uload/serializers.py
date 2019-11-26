from rest_framework import serializers
from uload.models import UploadMedia

class UloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadMedia
        fields = '__all__'
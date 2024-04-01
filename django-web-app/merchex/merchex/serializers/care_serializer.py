from rest_framework import serializers
from ..models import Care

class CareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Care
        fields = '__all__'
from .models import customers
from rest_framework import serializers

class customerserializer(serializers.ModelSerializer):
    class Meta:
        model = customers
        fields = '__all__'
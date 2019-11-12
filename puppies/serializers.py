from rest_framework import serializers
from .models import Puppy


class PuppySerializer(serializers.ModelSerializer):
    """
    Serializer for Puppy model
    """
    class Meta:
        """
        Metadata for PuppySerializer
        """
        model = Puppy
        fields = '__all__'

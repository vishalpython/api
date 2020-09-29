from rest_framework import serializers
from rest_framework import status


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing api"""
    name = serializers.CharField(max_length=10)

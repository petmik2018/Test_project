from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serialize name field for testing API views"""
    name = serializers.CharField(max_length=10)


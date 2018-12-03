from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serilalizes a name field for our APIView testing"""

    name = serializers.CharField(max_length=10)

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers

# Create your views here.

class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return a list of APIView features"""

        api_view = [
            'Uses HTTP methods as functions(get, put, post, delete, patch)',
            'It is similar to a traditional Django views.',
            'Gives most control over your logic',
            'Is mapped manually to Urls'
        ]


        return Response({'message':'Hello','api_view':api_view})

    def post(self, request):
       """ Create a hello message with our name"""
       serializer = serializers.HelloSerializer(data=request.data)
       if serializer.is_valid():
          name = serializer.data.get('name')
          message = 'Hello {0}'.format(name)
          return Response({'message':message})
       else:
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handles updating and object"""

        return Response({'message':'put'})

    def patch(self, request, pk=None):
        """Patch request, updates only the fields provided in the request"""

        return Response({'message':'patch'})

    def delete(self, request, pk=None):
        """Deletes and object ."""

        return Response({'message':'delete'})

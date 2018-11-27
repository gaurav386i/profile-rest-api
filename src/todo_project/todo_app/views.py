from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """Test API View"""

    def get(self, response, format=None):
        """Return a list of APIView features"""

        api_view = [
            'Uses HTTP methods as functions(get, put, post, delete, patch)',
            'It is similar to a traditional Django views.',
            'Gives most control over your logic',
            'Is mapped manually to Urls'
        ]


        return Response({'message':'Hello','api_view':api_view})
        

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from . import serializers
from . import models
from . import permissions

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



class HelloViewSet(viewsets.ViewSet):
    """Test API Viewset."""

    serializer_class = serializers.HelloSerializer

    def  list(self, request):

        a_viewset = [
          'Uses actions (list, create, retrieve, update ,partial_update )',
          'Automatically maps to URLs using Routers ',
          'Provides more functionality with less code.'
        ]

        return Response({'message':'Hello!','viewset':a_viewset})


    def create(self, request):
        """Create a new hello Message."""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'hello {0}'.format(name)
            return Response({'message': message})
        else:
           return Response(
           serializer.errors, status=status.HTTP_400_BAD_REQUEST )

    def retrieve(self, request, pk=None):
        """Retrieve Object by its ID"""

        return Response({'httpmethod':'GET'})

    def update(self, request, pk=None):
        """Handles updating an Object """

        return Response({'httpmethod':'PUT'})

    def partial_update(self, request, pk=None):
        """Handles updating an object Partially"""

        return Response({'httpmethod':'PATCH'})

    def destroy(self, request, pk=None):
        """Handels removing an Object"""

        return Response({'httpmethod':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handels creating and updating profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)


class LoginViewSet(viewsets.ViewSet):

    """Check email and password and return and token"""

    serializer_class = AuthTokenSerializer

    def create(self, request):

        """Use ObtainAuthToken API View to validate and create a token"""

        return ObtainAuthToken().post(request)

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handels creating , updating and reading profile feed items"""

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.PostOwnStatus, IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        """Sets the user profile to logged in User"""

        serializer.save(user_profile= self.request.user)

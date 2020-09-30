from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets
from profiles_api import models
from profiles_api import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.
class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer
    def get(self,request,format=None):
        """Return the list of APIview features"""
        an_apiview=[
        'Uses HTP methods as function (get,post,put,patch,delete)'
        'Is similar to a traditional Django View',
        'Gives you most control  over you applications',
        'Is mapped manually to urls'
        ]

        return Response({'message' : 'Hello!' , 'an_apiview' : an_apiview})
    def post(self,request):
        serializer =self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({"message" : message})
        else:
            return Response(
            serializer.errors,
            status = status.HTTP_404_BAD_REQUEST
            )


    def put(self,request,pk=None):
        """Handle updating hole object"""
        return Response({"message" : "PUT"})
    def patch(self,request,pk=None):
        """Handle partial updating object with specic field"""
        return Response({"message" : "patch"})

    def delete(self,request,pk=None):
        """Delete an object"""
        return Response({"method":"DELETE"})

class HelloViewset(viewsets.ViewSet):
    """Test API viewsets"""
    def list(self,request):
        a_viewsets = [
        'Uses action (list,creat,retrive,update,partial_update,destroy)',
        'Automatically maps to urls using Router',
        'Provided more functi..with less coading'
        ]
        return Response({"message" : a_viewsets})


    def create(self,request):
       """create a new hello messae"""
       serializer =self.serializer_class(data=request.data)
       if serializer.is_valid():
           name = serializer.validated_data.get('name')
           message = f'Hello {name}'
           return Response({"message" : message})
       else:
           return Response(
           serializer.errors,
           status = status.HTTP_404_BAD_REQUEST
           )
    def retrieve(self,request,pk=None):
        """Handle getting an objects by its ID"""
        return Response({"method" : "HTTP GET"})

    def update(self,request,pk=None):
        """Handlesupdating an  object"""
        return  Response({"method": "http_put"})

    def partial_update(self,request,pk=None):
       """Handle updating part of object"""
       return Response({"method":"http_patch"})
    def destroy(self,request,pk=None):
        """Handl remove of an object"""
        return Response({"method":"http_delete"})



class UserProfileViewset(viewsets.ModelViewSet):
    """Handl creating and updating profile"""
    serializer_class = serializers.UserProfileSerializer
    queryset =models.UserProfile.objects.all()

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)

class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewsets(viewsets.ModelViewSet):
    """Handle creating,updating reading profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.UserProfileFeedSerializer
    queryset = models.ProfileFeedItems.objects.all()
    permission_classes = (
    permissions.UpdateOwnStatus,
    IsAuthenticatedOrReadOnly
    )

    def perform_create(self,serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_proffile = self.request.user)

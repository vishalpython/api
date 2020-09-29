from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
    """Test API View"""
    def get(self,request,format=None):
        """Return the list of APIview features"""
        an_apiview=[
        'Uses HTP methods as function (get,post,put,patch,delete)'
        'Is similar to a traditional Django View',
        'Gives you most control  over you applications',
        'Is mapped manually to urls'
        ]

        return Response({'message' : 'Hello!' , 'an_apiview' : an_apiview})

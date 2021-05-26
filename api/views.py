from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView


class HelloAPI(generics.GenericAPIView):

    def get(self, request):
        """Return a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to traditional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview}, status=200)

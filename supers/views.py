from .serializers import SuperSerializer
from .models import Super
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

#class SuperList(generics.ListCreateAPIView):
#    queryset = Super.objects.all()
#    serializer_class = SuperSerializer

class SuperDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Super.objects.all()
    serializer_class = SuperSerializer

class SuperList(APIView):
    def get(self, request, format=None):
        super_type_name = request.query_params.get('type')
        queryset = Super.objects.all()
        if super_type_name:
            queryset = queryset.filter(super_type__type=super_type_name)
            type_serializer = SuperSerializer(queryset, many=True)
            return Response(type_serializer.data)
        custom_response = {}
        heroes = Super.objects.filter(super_type_id=1)
        villains = Super.objects.filter(super_type_id=2)
        hero_serializer = SuperSerializer(heroes, many=True)
        villain_serializer = SuperSerializer(villains, many=True)
        custom_response = {
            "Heroes": hero_serializer.data,
            "Villains": villain_serializer.data,
        }
        return Response(custom_response)

    def post(self, request, format=None):
        serializer = SuperSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


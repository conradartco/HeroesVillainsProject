from .serializers import SuperTypeSerializer
from .models import SuperType
from rest_framework import generics

class SuperTypeList(generics.ListCreateAPIView):
    queryset = SuperType.objects.all()
    serializer_class = SuperTypeSerializer

class SuperTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SuperType.objects.all()
    serializer_class = SuperTypeSerializer
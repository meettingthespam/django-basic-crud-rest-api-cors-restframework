from django.shortcuts import render

# generic views
from rest_framework import generics

from .models import Text_CRUD
from .serializers import Text_CRUD_Serializer

class ListText(generics.ListCreateAPIView):
    queryset = Text_CRUD.objects.all()
    serializer_class = Text_CRUD_Serializer

class DetailText(generics.RetrieveUpdateDestroyAPIView):
    queryset = Text_CRUD.objects.all()
    serializer_class = Text_CRUD_Serializer

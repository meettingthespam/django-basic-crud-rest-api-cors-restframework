from django.shortcuts import render

# generic views
from rest_framework import generics

from .models import Image_CRUD
from .serializers import Image_CRUD_Serializer

class ListImages(generics.ListCreateAPIView):
    queryset = Image_CRUD.objects.all()
    serializer_class = Image_CRUD_Serializer

class DetailImage(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image_CRUD.objects.all()
    serializer_class = Image_CRUD_Serializer

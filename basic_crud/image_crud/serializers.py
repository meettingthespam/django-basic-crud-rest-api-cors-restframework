from rest_framework import serializers
from .models import Image_CRUD

class Image_CRUD_Serializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Image_CRUD

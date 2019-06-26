from rest_framework import serializers
from .models import Text_CRUD


# serializers transalte our backend data
# into a format (JSON here) taht can be efficiently
# sent over the internet and used by another party
# in this case, it's our frontend. Who consumes (uses)
# the API is based on what permissions we set

class Text_CRUD_Serializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Text_CRUD

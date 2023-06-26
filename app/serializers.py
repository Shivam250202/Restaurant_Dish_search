from rest_framework import serializers

from app.models import *


class Restaurant_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant_Details
        fields = ['name','dish']
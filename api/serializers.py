from rest_framework import serializers
from .models import Clothing

class ClothingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clothing
        exclude = ['id']
from rest_framework import serializers
from .models import Element


class ElementsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Element
        fields = ("number", )

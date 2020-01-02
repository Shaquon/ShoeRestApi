from shoes.models import Shoe, ShoeType, ShoeColor, Manufacturer
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer


class ManufacturerSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['id', 'name', 'website']


class ShoeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Shoe
        fields = ['size', 'brand', 'manufacturer', 'color','material', 'shoe_type']


class ShoeTypeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ShoeType
        fields = ['style']


class ShoeColorSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ShoeColor
        fields = ['color_style']

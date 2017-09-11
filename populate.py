#!/usr/bin/env python
"""
:created on: 31-08-2017
:modified on: 11-09-2017
:author: Miranda Aperghis <miranda>
:contact: miranda.aperghis@gmail.com
"""
from backpackers.models import Person
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):
    """Person serializer"""
    first_name = serializers.CharField(source='firstName')
    last_name = serializers.CharField(source='lastName')
    eye_colour = serializers.CharField(source='eyeColour')
    distance_travelled = serializers.CharField(source='distance')

    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'age', 'gender', 'eye_colour',
        'nationality', 'email', 'phone', 'states', 'distance_travelled',
        'transport', 'days', 'working')

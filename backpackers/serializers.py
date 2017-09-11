#!/usr/bin/env python
"""
:created on: 31-08-2017
:modified on: 11-09-2017
:author: Miranda Aperghis <miranda>
:contact: miranda.aperghis@gmail.com
"""
from backpackers.models import Person, State, Transport
from rest_framework import serializers


class StateSerializer(serializers.ModelSerializer):
    """State serializer"""
    class Meta:
        model = State
        fields = ('name',)


class TransportSerializer(serializers.ModelSerializer):
    """Transport serializer"""
    class Meta:
        model = Transport
        fields = ('mode',)


class PersonSerializer(serializers.ModelSerializer):
    """Person serializer"""
    class Meta:
        model = Person
        fields = ('firstName', 'lastName', 'age', 'gender', 'eyeColour',
            'nationality', 'email', 'phone', 'states', 'distance',
            'transport', 'days', 'working')

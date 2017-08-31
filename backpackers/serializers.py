from rest_framework import serializers
from backpackers.models import Person, State, Transport


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ('name',)


class TransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transport
        fields = ('mode',)


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('firstName', 'lastName', 'age', 'gender', 'eyeColour',
            'nationality', 'email', 'phone', 'states', 'distance',
            'transport', 'days', 'working')

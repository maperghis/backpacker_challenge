from rest_framework import serializers
from backpackers.models import Person


class PersonSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='firstName')
    last_name = serializers.CharField(source='lastName')
    eye_colour = serializers.CharField(source='eyeColour')
    distance_travelled = serializers.CharField(source='distance')

    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'age', 'gender', 'eye_colour',
        'nationality', 'email', 'phone', 'states', 'distance_travelled',
        'transport', 'days', 'working')

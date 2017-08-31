from rest_framework import serializers
from backpackers.models import Person, GENDER_CHOICES, EYE_COLOUR_CHOICES, \
    NATIONALITY_CHOICES

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('firstName', 'lastName', 'age', 'gender', 'eyeColour',
            'nationality', 'email', 'phone', 'states', 'distance',
            'transport', 'days', 'working')

from backpackers.models import Person, State, Transport
from backpackers.serializers import PersonSerializer, StateSerializer, \
    TransportSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics


class PersonList(generics.ListAPIView):
    '''List all the people'''
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonDetail(APIView):
    '''Retrieve a person instance'''

    def getObject(self, name):
        try:
            firstName, lastName = name.split(' ')
            return Person.objects.get(firstName=firstName, lastName=lastName)
        except Person.DoesNotExist as exc:
            raise Http404

    def get(self, request, name):
        person = self.getObject(name)
        serializer = PersonSerializer(person)
        return Response(serializer.data)


class StateList(generics.ListAPIView):
    '''List all the states'''
    queryset = State.objects.all()
    serializer_class = StateSerializer


class StateDetail(generics.RetrieveAPIView):
    '''Retrieve a state instance'''
    queryset = State.objects.all()
    serializer_class = StateSerializer
    lookup_field = 'name'


class TransportList(generics.ListAPIView):
    '''Retrieve all the transport modes'''
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer


class TransportDetail(generics.RetrieveAPIView):
    '''Retrieve a transport instance'''
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer
    lookup_field = 'mode'

from backpackers.models import Person, State, Transport
from backpackers.serializers import PersonSerializer, StateSerializer, \
    TransportSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class PersonList(APIView):
    '''List all the people'''

    def get(self, request):
        people = Person.objects.all()
        serializer = PersonSerializer(people, many=True)
        return Response(serializer.data)


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


class StateList(APIView):
    '''List all the states'''

    def get(self, request):
        states = State.objects.all()
        serializer = StateSerializer(states, many=True)
        return Response(serializer.data)


class StateDetail(APIView):
    '''Retrieve a state instance'''

    def getObject(self, name):
        try:
            return State.objects.get(name=name)
        except State.DoesNotExist as exc:
            raise Http404

    def get(self, request, name):
        state = self.getObject(name)
        serializer = StateSerializer(state)
        return Response(serializer.data)


class TransportList(APIView):
    '''Retrieve all the transport modes'''

    def get(self, request):
        modes = Transport.objects.all()
        serializer = TransportSerializer(modes, many=True)
        return Response(serializer.data)


class TransportDetail(APIView):
    '''Retrieve a transport instance'''

    def getObject(self, mode):
        try:
            return Transport.objects.get(mode=mode)
        except Transport.DoesNotExist as exc:
            raise Http404

    def get(self, request, mode):
        name = self.getObject(mode)
        serializer = TransportSerializer(name)
        return Response(serializer.data)

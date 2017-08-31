from django.http import HttpResponse
from backpackers.models import Person, State, Transport
from backpackers.serializers import PersonSerializer, StateSerializer, \
    TransportSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def personList(request):
    '''List all people'''
    if request.method == 'GET':
        people = Person.objects.all()
        serializer = PersonSerializer(people, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def personDetail(request, name):
    '''Retrieve a person'''
    try:
        firstName, lastName = name.split(' ')
        person = Person.objects.get(firstName=firstName, lastName=lastName)
    except Person.DoesNotExist as exc:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PersonSerializer(person)
        return Response(serializer.data)

@api_view(['GET'])
def stateList(request):
    '''List all states'''
    if request.method == 'GET':
        states = State.objects.all()
        serializer = StateSerializer(states, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def stateDetail(request, name):
    '''Retreive a state'''
    try:
        state = State.objects.get(name=name)
    except Stae.DoesNotExist as exc:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StateSerializer(state)
        return Response(serializer.data)

@api_view(['GET'])
def transportList(request):
    '''List all transport modes'''
    if request.method == 'GET':
        modes = Transport.objects.all()
        serializer = TransportSerializer(modes, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def transportDetail(request, mode):
    '''Retreive a transport mode'''
    try:
        state = Transport.objects.get(mode=mode)
    except Transport.DoesNotExist as exc:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TransportSerializer(state)
        return Response(serializer.data)

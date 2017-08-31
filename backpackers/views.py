from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from backpackers.models import Person, State, Transport
from backpackers.serializers import PersonSerializer, StateSerializer, \
    TransportSerializer


def index(request):
    return HttpResponse("Hello, world!")

@csrf_exempt
def personList(request):
    '''List all people'''
    if request.method == 'GET':
        people = Person.objects.all()
        serializer = PersonSerializer(people, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def personDetail(request, name):
    '''Retrieve a person'''
    try:
        firstName, lastName = name.split(' ')
        person = Person.objects.get(firstName=firstName, lastName=lastName)
    except Exception as exc:
        return HttpResponse(exc)

    if request.method == 'GET':
        serializer = PersonSerializer(person)
        return JsonResponse(serializer.data)

@csrf_exempt
def stateList(request):
    '''List all states'''
    if request.method == 'GET':
        states = State.objects.all()
        serializer = StateSerializer(states, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def stateDetail(request, name):
    '''Retreive a state'''
    try:
        state = State.objects.get(name=name)
    except Exception as exc:
        return HttpResponse(exc)

    if request.method == 'GET':
        serializer = StateSerializer(state)
        return JsonResponse(serializer.data)

@csrf_exempt
def transportList(request):
    '''List all transport modes'''
    if request.method == 'GET':
        modes = Transport.objects.all()
        serializer = TransportSerializer(modes, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def transportDetail(request, mode):
    '''Retreive a transport mode'''
    try:
        state = Transport.objects.get(mode=mode)
    except Exception as exc:
        return HttpResponse(exc)

    if request.method == 'GET':
        serializer = TransportSerializer(state)
        return JsonResponse(serializer.data)

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from backpackers.models import Person
from backpackers.serializers import PersonSerializer


def index(request):
    return HttpResponse("Hello, world!")


@csrf_exempt
def personList(request):
    '''List all people'''
    if request.method == 'GET':
        snippets = Person.objects.all()
        serializer = PersonSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def personDetail(request, name):
    '''Retrieve a person'''
    try:
        print name
        firstName, lastName = name.split(' ')
        person = Person.objects.get(firstName=firstName, lastName=lastName)
    except Exception as exc:
        return HttpResponse(exc)

    if request.method == 'GET':
        serializer = PersonSerializer(person)
        return JsonResponse(serializer.data)

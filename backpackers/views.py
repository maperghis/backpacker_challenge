#!/usr/bin/env python
"""
:created on: 31-08-2017
:modified on: 11-09-2017
:author: Miranda Aperghis <miranda>
:contact: miranda.aperghis@gmail.com
"""
from backpackers.models import Person, State, Transport
from backpackers.serializers import PersonSerializer, StateSerializer, \
    TransportSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets


class PersonList(generics.ListAPIView):
    """List all the people"""
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonDetail(APIView):
    """Retrieve a person instance"""

    def getObject(self, name):
        """Get an object given the full name"""
        try:
            firstName, lastName = name.split(' ')
            return Person.objects.get(firstName=firstName, lastName=lastName)
        except Person.DoesNotExist as exc:
            raise Http404

    def get(self, request, name):
        """Take a request with a name and return a response"""
        person = self.getObject(name)
        serializer = PersonSerializer(person)
        return Response(serializer.data)


class StateViewSet(viewsets.ReadOnlyModelViewSet):
    """List and retrieve states"""
    queryset = State.objects.all()
    serializer_class = StateSerializer
    lookup_field = 'name'


class TransportViewSet(viewsets.ReadOnlyModelViewSet):
    """List and retrieve transport models"""
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer
    lookup_field = 'mode'

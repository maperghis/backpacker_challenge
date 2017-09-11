#!/usr/bin/env python
"""
:created on: 31-08-2017
:modified on: 11-09-2017
:author: Miranda Aperghis <miranda>
:contact: miranda.aperghis@gmail.com
"""
from django.contrib import admin
from backpackers.models import State, Transport, Person


admin.site.register(State)
admin.site.register(Transport)
admin.site.register(Person)

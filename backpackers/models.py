#!/usr/bin/env python
"""
:created on: 31-08-2017
:modified on: 11-09-2017
:author: Miranda Aperghis <miranda>
:contact: miranda.aperghis@gmail.com
"""
from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, \
    MaxValueValidator

GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))
EYE_COLOUR_CHOICES = (('Br', 'Brown'), ('Bl', 'Blue'))
NATIONALITY_CHOICES = (
    ('Br', 'British'),
    ('Fr', 'French'),
    ('Gr', 'German'),
    ('Sp', 'Spanish'),
    ('It', 'Italian'),
    ('Sw', 'Swiss'),
    ('Cn', 'Canadian'),
)


class State(models.Model):
    """State model"""
    name = models.CharField(max_length=300,
            verbose_name="name of state or territory")

    def __unicode__(self):
        return self.name


class Transport(models.Model):
    """Transport model"""
    mode = models.CharField(max_length=300,
            verbose_name="mode of transport")

    def __unicode__(self):
        return self.mode


class Person(models.Model):
    """Person model"""
    firstName = models.CharField(max_length=300, verbose_name="first name")
    lastName = models.CharField(max_length=300, verbose_name="last name")
    age = models.IntegerField(validators=[MinValueValidator(18),
        MaxValueValidator(30)])
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    eyeColour = models.CharField(max_length=2, choices=EYE_COLOUR_CHOICES,
        default='Br', verbose_name="eye colour")
    nationality = models.CharField(max_length=2, choices=NATIONALITY_CHOICES,
        default='Br')
    email = models.EmailField(max_length=254, verbose_name="email address")
    phone = models.CharField(max_length=254, verbose_name="phone number")
    states = models.ManyToManyField(State, related_name="people_states")
    distance = models.IntegerField(default=1, validators=[MinValueValidator(1),
        MaxValueValidator(100000)])
    transport = models.ManyToManyField(Transport,
        related_name="people_transports")
    days = models.IntegerField(default=1, validators=[MinValueValidator(1),
        MaxValueValidator(720)])
    working = models.BooleanField(default=False)

    def __unicode__(self):
        return ' '.join([self.firstName, self.lastName])

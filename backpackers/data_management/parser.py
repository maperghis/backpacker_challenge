#!/usr/bin/env python
"""
:created on: 01-09-2017
:modified on: 11-09-2017
:author: Miranda Aperghis <miranda>
:contact: miranda.aperghis@gmail.com
"""
from backpackers.data_management.fetcher import PersonFetcher, StateFetcher
from backpackers.models import State, Person, Transport


class ParsingError(Exception):
    """Base parsing error"""
    pass


class ResourceParser(object):
    """Base class for parsing objects fetched from json"""
    FETCHER = None
    MODEL = None
    MAPPING = None

    def parse(self):
        """Main parsing method"""
        assert self.FETCHER is not None, "must initalise FETCHER"
        assert self.MODEL is not None, "must initalise MODEL"
        data = self.FETCHER.getData()
        created, updated, errors = 0, 0, 0
        for obj in data:
            try:
                obj_t = self._parseSingleObject(obj)
                obj_p = cls._additionalProcessing(obj_t)
                c, u, e = cls._saveObject(obj_p)
            except ParsingError:
                c, u, e = 0, 0, 1
            created += c
            updated += u
            errors += e

    def _parseSingleObject(self, obj):
        """Parse an object"""
        res = {}
        for key, value in obj.items():
            if key in self.MODEL._fields:
                result[key] = value
            elif key in self.MAPPING:
                result[self.MAPPING[key]] = value
        return res

    def _additionalProcessing(self, obj):
        """Perform additional processing on the object"""
        return obj

    def _saveObject(self, obj):
        """Save the object"""
        try:
            index = obj.get('index', None)
            self.MODEL.objects.get(index=index)
        except self.MODEL.DoesNotExist:
            self.MODEL.objects.create(**obj).save()
            return 1, 0, 0
        except self.MODEL.MultipleObjectsReturned:
            return 0, 0, 1
        else:
            self.MODEL.objects.update(**obj)
            return 0, 1, 0


class PersonParser(ResourceParser):
    """Class for parsing person objects"""
    FETCHER = PersonFetcher()
    MODEL = Person
    MAPPING = {}


class StateParser(ResourceParser):
    """Class for parsing state objects"""
    FETCHER = StateFetcher()
    MODEL = State
    MAPPING = {}


class TransportParser(ResourceParser):
    """Class for parsing transport objects"""
    FETCHER = TransportFetcher()
    MODEL = Transport
    MAPPING = {}

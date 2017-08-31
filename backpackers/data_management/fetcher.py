from django.conf import settings
import json
import os


class InvalidResourceError(Exception):
    pass


class ResourceFetcher(object):
    '''Base class for fetching json data from a file'''
    FILE = None
    RESOURCE_DIR = os.path.join(settings.BASE_DIR, 'resources')

    def __init__(self):
        assert self.FILE is not None, "must initialise FILE"
        self._file = os.path.join(self.RESOURCE_DIR, self.FILE)

    def getData(self):
        '''Load the json file and return the resulting python object'''
        try:
            with open(self._file, 'r') as f:
                content = f.read()
        except IOError:
            raise InvalidResourceError("File %s does not exist" % self._file)
        try:
            data = json.loads(content)
        except (TypeError, ValueError):
            raise InvalidResourceError("File %s is corrupted, doesn't contain "
                "valid json" % self._file)
        data = [data] if not isinstance(data, list) else data
        return data


class PeopleFetcher(ResourceFetcher):
    '''Fetcher for the people data'''
    FILE = 'person.json'


class StateFetcher(ResourceFetcher):
    '''Fetcher for the state data'''
    FILE = 'state.json'


class TransportFetcher(ResourceFetcher):
    '''Fetcher for the transport data'''
    FILE = 'transport.json'

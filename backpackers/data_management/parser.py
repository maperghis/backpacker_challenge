from backpackers.data_management.fetcher import PersonFetcher, StateFetcher


class ParsingError(Exception):
    pass


class ResourceParser(object):
    '''Base class for parsing objects fetched from json'''
    FETCHER = None

    def parse(self):
        '''Main parsing method'''
        assert self.FETCHER is not None, "must initalise FETCHER"
        data = self.FETCHER.getData()


class PersonParser(ResourceParser):
    '''Class for parsing person objects'''
    FETCHER = PersonFetcher()


class StateParser(ResourceParser):
    '''Class for parsing state objects'''
    FETCHER = StateFetcher()

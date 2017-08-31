from django.test import TestCase
from backpackers.data_management.fetcher import PeopleFetcher


class TestFetcher(TestCase):
    '''Tests for the fetcher class'''

    def test_getData(self):
        fetcher = PeopleFetcher()
        self.assertIsInstance(fetcher.getData(), list)

from django.test import TestCase
from backpackers.data_management.fetcher import PersonFetcher


class TestFetcher(TestCase):
    '''Tests for the fetcher class'''

    def test_getData(self):
        fetcher = PersonFetcher()
        self.assertIsInstance(fetcher.getData(), list)

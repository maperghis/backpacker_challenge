#!/usr/bin/env python
"""
:created on: 31-08-2017
:modified on: 11-09-2017
:author: Miranda Aperghis <miranda>
:contact: miranda.aperghis@gmail.com
"""
from django.test import TestCase
from backpackers.data_management.fetcher import PersonFetcher


class TestFetcher(TestCase):
    """Tests for the fetcher class"""

    def test_getData(self):
        """Test for getData"""
        fetcher = PersonFetcher()
        self.assertIsInstance(fetcher.getData(), list)

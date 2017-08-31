from django.core.management.base import BaseCommand
from blogapp.models import Post, Tag


class Command(BaseCommand):
    '''Additional command to populate the database'''

    def handle(self, *args, **kwargs):
        '''Main method for populating the database'''
        self.stdout.write('Populating database.')
        self.stdout.write('Populating states.')
        # populate states here
        self.stdout.write('Populating transport.')
        # populate transport here
        self.stdout.write('Populating people.')
        # populate people here
        self.stdout.write('Finished populating database.')

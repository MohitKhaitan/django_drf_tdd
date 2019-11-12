from django.test import TestCase
from puppies.models import Puppy


class PuppyTest(TestCase):
    """ Test module for Puppy model"""

    def setUp(self) -> None:
        """ Adding dummy entries to the table """
        Puppy.objects.create(name='Casper', age=3, breed='Bull Dog', color='Black')
        Puppy.objects.create(name='Muffin', age=1, breed='Gradane', color='Brown')

    def test_puppy_breed(self):
        """ Test for Puppy breed"""
        puppy_casper = Puppy.objects.get(name='Casper')
        puppy_muffin = Puppy.objects.get(name='Muffin')

        self.assert_(puppy_casper.get_breed(), 'Casper belongs to Bull Dog breed.')
        self.assert_(puppy_muffin.get_breed(), 'Muffin belongs to Gradane breed')



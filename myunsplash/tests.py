from django.test import TestCase

# importation of models
from .models import Image,Location,Category


# Create your tests here.
class LocationTestClass(TestCase):
    """
    Test class for testing location model
    """

    # setup method
    def setUp(self):
        """
        setup method creating instance of location class
        :return:
        """
        self.Kisumu = Location(locale='Kisumu')

    # Testing instance
    def test_instance(self):
        """
        confirming correct instantiation of object
        :return:
        """
        self.assertTrue(isinstance(self.Kisumu, Location))

    # Testing deletion of category
    def tearDown(self):
        Location.objects.all().delete()


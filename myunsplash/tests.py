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


class ImageTestClass(TestCase):
    """
    test class to test image model
    """
    def setUp(self):
        """
        testing instantiation and saving of image
        :return:
        """
        # creation of category
        self.new_category = Category(name='Travel')
        self.new_category.save()

        self.new_location = Location(locale='Kisumu')
        self.new_location.save()

        self.new_image = Image(Name='image1', Description='my first image', location='Kisumu', category='Travel')
        self.new_image.save()

        self.new_image.location.add(self.new_location)
        self.new_category.category.add(self.new_category)

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()

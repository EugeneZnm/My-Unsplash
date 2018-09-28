from django.db import models


# Create your models here.
class Image(models.Model):
    """
    Image class creating table for Image
    """
    Name = models.CharField(max_length=20)
    Description = models.CharField(max_length=40)
    image =  models.ImageField(upload_to='images/', blank=True)
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    Category = models.ManyToManyField(Category)

    def save_image(self):
        """
        method to save image and its details
        :return:
        """
        self.save()

    def delete_image(self):
        """
        method to delete image and details
        :return:
        """
        self.delete()

    @classmethod
    def search_by_category(cls, category):
        """
        method to search for image by category
        :return:
        """
        image = cls.object.filter(name__contains=category)
        return image

    @classmethod
    def location_filter(cls, location):
        """
        method to filter image by id
        :return:
        """
        image = cls.object.filter(location=location)
        return image

    @classmethod
    def get_image(cls):
        """
        method to get image by id
        :return:
        """
        id = image.name()
        images = cls.objects.filter(name=id)
        return images


class Location(models.Model):
    """
    class to save location of where the photograph was taken
    """
    locale = models.CharField(max_length=20)

    def save_location(self):
        """
        method to save location
        :return:
        """
        self.save()

    def __str__(self):
        return self.locale


class Category(models.Model):
    """
    category model to save image categories
    """
    category = models.CharField(max_length=10)

    def __str__(self):
        return self.category

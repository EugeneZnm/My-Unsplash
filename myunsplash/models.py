from django.db import models


# Create your models here.


class Location(models.Model):
    """
    class to save location of where the photograph was taken
    """
    locale = models.CharField(max_length=300)

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
    category = models.CharField(max_length=1000)

    def __str__(self):
        return self.category


class Image(models.Model):
    """
    Image class creating table for Image
    """
    Name = models.CharField(max_length=200)
    Description = models.CharField(max_length=4000)
    By = models.CharField(max_length=1000, default=True)
    image = models.ImageField(upload_to='images/', blank=True)
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category, default=True)

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
    def search_by_category(cls, search_term):
        """
        method to search for image by category
        :return:
        """
        image = cls.objects.filter(category__category__icontains=search_term)
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
        method to get  all images
        :return:
        """
        images = cls.objects.all()
        return images

    @classmethod
    def single_image(cls, image_id):
        """
        method to get images by id
        :return:
        """
        images = cls.objects.filter(id=image_id)
        return images




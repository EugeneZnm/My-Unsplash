from django.db import models


# Create your models here.
class Image(models.Model):
    """
    Image class creating table for Image
    """
    id = models.IntegerField()
    Name = models.CharField(max_length=20)
    Description = models.CharField(max_length=40)

    def save_image(self):
        """
        method to save image and its details
        :return:
        """
        self.save()

    @classmethod
    def search_by_name(cls, search_term):
        """
        method to search for image
        :return:
        """
        image = cls.object.filter(name__contains=search_term)
        return image

    @classmethod
    def image_filter(cls, id):
        """
        method to filter image by id
        :return:
        """
        image = cls.object.filter(id=id)
        return image

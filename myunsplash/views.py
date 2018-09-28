from django.shortcuts import render, redirect

# importation of HttpResponse from django
from django.http import HttpResponse

from .models import Image, Location, Category


# Create your views here.
def Home(request):
    images = Image.get_image()
    for x in images:
        print(x.image)
    return render(request, 'index.html',{"images":images})


# view function to represent
def single_image(request, image_id):
    pics = Image.objects.get(id=image_id)
    return render(request, 'single-image.html', {"pics":pics})








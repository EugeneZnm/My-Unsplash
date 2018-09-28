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


# search images
def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term =request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message, "images":searched_images})

    else:
        message ="Enter Category to Search For"
        return render(request, "search.html", {"message":message})





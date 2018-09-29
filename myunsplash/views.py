from django.shortcuts import render, redirect

from .models import Image, Location, Category


# Create your views here.
def Home(request):
    images = Image.get_image()
    for x in images:
        print(x.image)
    location = Location.objects.all()
    return render(request, 'index.html',{"images":images, "location":location} )


# view function for single image
def single_image(request, image_id):
    images = Image.single_image(image_id)
    return render(request, 'Image/single-image.html', {"images":images, "image_id":image_id})


# search images
def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term =request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'Image/search.html',{"message":message, "images":searched_images})

    else:
        message ="Enter Category to Search For"
        return render(request, "Image/search.html", {"message":message})





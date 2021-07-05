from django.http.response import Http404
from django.shortcuts import render
from .models import Image, Location

# Create your views here.

#landing_page
def landing_page(request):
    images = Image.all_images()
    locations = Location.objects.all()
    return render(request, 'landing.html', {"images":images[::-1],"locations":locations})

#image_location function to find the image results by location.
def location(request,location):
    # locations = Location.objects.all()
    # selected_location = Location.objects.get(id = location)
    # images = Image.objects.filter(location = selected_location.id)
    locations = Image.filter_by_location(location)
    return render(request,'location.html',{"locations":locations}) 

#image view function to find the image results by id.
def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except Exception:
        
        raise Http404()
    return render(request,"image.html", {"image":image})


#search view function of the results.
def search_results(request):
    if 'image_search' in request.GET and request.GET["image_search"]:
        category = request.GET.get("image_search")
        searched_images = Image.search_by_category(category)
        message = f"{category}"
       
        return render(request,'search.html', {"message": message, "images": searched_images})
    else:
        message = "You haven't searched for any image category present"
        return render(request,'search.html', {"message": message})


from django.http.response import Http404
from django.shortcuts import render
from .models import Image, Location

# Create your views here.
#landing_page
def landing_page(request):
    images = Image.objects.all()
    locations = Location.get_image_locations()

    return render(request,'landing.html')

#search view function of the results
def search_results(request):
    if 'image_search' in request.GET and request.GET["image_search"]:
        category = request.GET.get("image_search")
        searched_images = Image.search_by_category(category)
        message = f"{category}"
       
        return render(request,'search.html', {"message": message, "images": searched_images})
    else:
        message = "You haven't searched for any image category present"
        return render(request,'search.html', {"message": message})

def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except Exception:
        
        raise Http404()
    return render(request,"image.html", {"image":image})
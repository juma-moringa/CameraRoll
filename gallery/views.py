from django.shortcuts import render
from .models import Image, Location

# Create your views here.
#landing_page
def landing_page(request):
    images = Image.objects.all()
    locations = Location.get_image_locations()

    return render(request,'landing.html',{ 'locations': locations})


#search view function of the results
def search_results(request):
    if 'imagesearch' in request.GET and request.GET["imagesearch"]:
        category = request.GET.get("imagesearch")
        searched_images = Image.search_by_category(category)
        message = f"{category}"
       
        return render(request,'search-results.html', {"message": message, "images": searched_images})
    else:
        message = "You haven't searched for any image category present"
        return render(request,'search-results.html', {"message": message})


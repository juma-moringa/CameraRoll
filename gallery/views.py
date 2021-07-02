from django.shortcuts import render
from .models import Image, Location

# Create your views here.
#landing_page
def landing_page(request):
    images = Image.objects.all()
    locations = Location.get_image_locations()
    return render(request,'landing.html',{ 'locations': locations})
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

#2nd (Location class)
class Location(models.Model):
    name = models.CharField(max_length=100)        

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()    

    @classmethod
    def get_image_locations(cls):
        locations = Location.objects.all()
        return locations
    


#3rd  (Category Class)  
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()    

# 1st(Image class) 
class Image(models.Model):
    # image=models.ImageField(upload_to='images/')
   
    image_name=models.CharField(max_length=200)
    image = CloudinaryField('image')
    description=models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default='0')
    location = models.ForeignKey(Location,on_delete=models.CASCADE,default='0')

    
    def __str__(self):
        return self.image_name

    #function to save the image.
    def save_image(self):
        self.save()

    #function to delete the image.
    def delete_image(self):
        self.delete()

    #defined the search function.
    @classmethod
    def search_by_category(cls, category):
        images = cls.objects.filter(category__name__icontains=category)
        return images

    #function to update the image.
    @classmethod
    def update_image(cls, id, image):
        cls.objects.filter(id=id).update(image=image)

    #function to get the image by id.
    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id=id).all()
        return image
    #function to get all the images and display in the landing page.    
    @classmethod
    def all_images(cls):
        images = cls.objects.all()
        return images

    #function to filter the image by location.   
    @classmethod
    def filter_by_location(cls, location):
        image_location = cls.objects.filter(location__name=location).all()
        return image_location

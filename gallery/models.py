from django.db import models

# Create your models here.

#2nd class
class Location(models.Model):
    name = models.CharField(max_length=100)        

    def __str__(self):
        return self.name


#3rd Class   
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()    

# 1st class
class Image(models.Model):
    image=models.ImageField(upload_to='images/')
    image_name=models.CharField(max_length=200)
    description=models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default='0')
    location = models.ForeignKey(Location ,on_delete=models.CASCADE,default='0')

    
    def __str__(self):
        return self.name
        
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    
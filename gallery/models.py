from django.db import models

# Create your models here.
# 1st class
class Image(models.Model):
    image=models.ImageField(upload_to='images/')
    image_name=models.CharField(max_length=200)
    description=models.TextField()
    # location=models.ForeignKey()
    # category=models.ForeignKey()

    
    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=60)        

    def __str__(self):
        return self.name
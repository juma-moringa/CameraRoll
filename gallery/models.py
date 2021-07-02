from django.db import models

# Create your models here.
# 1st class
class Image(models.Model):
    image=models.ImageField(upload_to='images/')
    image_name=models.CharField(max_length=200)
    description=models.TextField()
    # location=models.ForeignKey()
    # category=models.ForeignKey()



#2nd class
class Location(models.Model):
    name = models.CharField(max_length=100)


#3rd class
class Category(models.Model):
    name = models.CharField(max_length=50)    
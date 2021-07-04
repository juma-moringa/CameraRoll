from gallery.models import Category, Image, Location
from django.test import TestCase

# Create your tests here.

#test1
class TestLocation(TestCase):
    def setUp(self):
        self.location = Location(name='Area 4')
        self.location.save_location()

    def test_instance(self):
        self.location.save()
        self.assertTrue(isinstance(self.location, Location))

    def test_save_location(self):
        self.location.save_location()
        location_test = Location.get_image_locations()
        self.assertTrue(len(location_test) > 0)

    def test_get_image_locations(self):
        self.location.save_location()
 
        self.location.save_location()
        location_test = Location.get_image_locations()
        self.assertFalse(len(location_test) > 1)

    def test_delete_location(self):
        self.location.delete_location()
        location_test = Location.objects.all()
        self.assertTrue(len(location_test) == 0) 


#test2
class CategoryTest(TestCase):
    def setUp(self):
        self.category = Category(name='rap')
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        self.category.save_category()
        category_name = Category.objects.all()
        self.assertTrue(len( category_name) > 0)

    def test_delete_category(self): 
        self.category.delete_category()
        category_name = Category.objects.all()
        self.assertTrue(len(category_name))  



from gallery.models import Category, Image, Location
from django.test import TestCase

# Create your tests here.

#test1
class TestImage(TestCase):
    def setUp(self):
        self.location = Location(name='East side')
        self.location.save_location()
        self.category = Category(name='rap')
        self.category.save_category()
        self.image = Image(id=1, image_name='image', description='The Wakadinali group is definitely going to take Kenyan rap music to the next level as most people consider them as the best rap group in East',location=self.location,category=self.category)

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))    

    def test_save_image(self):
            self.image.save_image()
            images = Image.objects.all()
            self.assertTrue(len(images) > 0)

    def test_delete_image(self):
            self.image.delete_image()
            images = Image.objects.all()
            self.assertTrue(len(images) == 0) 

    def test_update_image(self):
            self.image.save_image()
            self.image.update_image(self.image.id, 'media/images/logoo.jpg')
            updated_image = Image.objects.filter(image='media/images/images.png')
            self.assertFalse(len(updated_image) > 0)
   
    def test_get_image_by_id(self):
            found_image = self.image.get_image_by_id(self.image.id)
            images = Image.objects.filter(id=self.image.id)
            self.assertFalse(found_image, images)  

    def test_search_by_category(self):
            category = 'rap'
            found_image = self.image.search_by_category(category)
            self.assertFalse(len(found_image) > 1) 

    
    def tearDown(self):
            Image.objects.all().delete()
            Location.objects.all().delete()
            Category.objects.all().delete()

#test2
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


#test3
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
        self.assertTrue(len(category_name) == 0)  



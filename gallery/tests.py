from gallery.models import Category
from django.test import TestCase

# Create your tests here.

#test1
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
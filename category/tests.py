from category.models import Category
from django.test import TestCase


class CategoryCreate(TestCase):

    def create_category(self, name="Category", description="Category description"):
        return Category.objects.create(name=name, description=description)

    def test_create_category(self):
        category = self.create_category()
        self.assertTrue(isinstance(category, Category))
        self.assertEqual(category.__str__(), category.name)

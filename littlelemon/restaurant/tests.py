from django.test import TestCase
from .models import MenuItem

class MenuItemTest(TestCase):
    def setUp(self):
        MenuItem.objects.create(name="Test Item", description="Test Description", price=9.99)

    def test_menu_item_creation(self):
        item = MenuItem.objects.get(name="Test Item")
        self.assertEqual(item.description, "Test Description")

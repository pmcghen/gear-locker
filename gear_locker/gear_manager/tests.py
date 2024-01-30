from django.test import TestCase

from .models import GearListItem

class GearListItemTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.item = GearListItem.objects.create(
            name='Test Item',
            description='Test Description',
            quantity=1,
            price=100.00,
            weight=1.00,
            url='http://www.test.com',
            is_worn=False,
            is_consumable=False,
            is_favorite=False,
        )

    def test_name_content(self):
        self.assertEqual(self.item.name, 'Test Item')

    def test_description_content(self):
        self.assertEqual(self.item.description, 'Test Description')

    def test_quantity_content(self):
        self.assertEqual(self.item.quantity, 1)

    def test_price_content(self):
        self.assertEqual(self.item.price, 100.00)

    def test_weight_content(self):
        self.assertEqual(self.item.weight, 1.00)

    def test_url_content(self):
        self.assertEqual(self.item.url, 'http://www.test.com')

    def test_is_worn_content(self):
        self.assertEqual(self.item.is_worn, False)

    def test_is_consumable_content(self):
        self.assertEqual(self.item.is_consumable, False)

    def test_is_favorite_content(self):
        self.assertEqual(self.item.is_favorite, False)

    def test_price_max_digits(self):
        item = GearListItem.objects.get(id=1)
        max_digits = item._meta.get_field('price').max_digits
        self.assertEqual(max_digits, 6)

    def test_price_decimal_places(self):
        item = GearListItem.objects.get(id=1)
        decimal_places = item._meta.get_field('price').decimal_places
        self.assertEqual(decimal_places, 2)

    def test_weight_max_digits(self):
        item = GearListItem.objects.get(id=1)
        max_digits = item._meta.get_field('weight').max_digits
        self.assertEqual(max_digits, 6)

    def test_weight_decimal_places(self):
        item = GearListItem.objects.get(id=1)
        decimal_places = item._meta.get_field('weight').decimal_places
        self.assertEqual(decimal_places, 2)

    def test_is_worn_default(self):
        item = GearListItem.objects.get(id=1)
        default = item._meta.get_field('is_worn').default
        self.assertEqual(default, False)

    def test_is_consumable_default(self):
        item = GearListItem.objects.get(id=1)
        default = item._meta.get_field('is_consumable').default
        self.assertEqual(default, False)

    def test_is_favorite_default(self):
        item = GearListItem.objects.get(id=1)
        default = item._meta.get_field('is_favorite').default
        self.assertEqual(default, False)

    def test_image_upload_to(self):
        item = GearListItem.objects.get(id=1)
        upload_to = item._meta.get_field('image').upload_to
        self.assertEqual(upload_to, 'images/')

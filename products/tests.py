from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Product

class ProductAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.product_data = {
            'name': 'Test Product',
            'description': 'Test Description',
            'price': 99.99,
            'stock': 10
        }

    def test_create_product(self):
        response = self.client.post('/api/products/', self.product_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().name, 'Test Product')

    def test_list_products(self):
        Product.objects.create(**self.product_data)
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
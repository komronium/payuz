from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status
from rest_framework.test import APITestCase

from product.models import Product, ProductImage


class ProductAPITests(APITestCase):

    def setUp(self):
        self.active_product = Product.objects.create(
            name="Lag'an",
            name_ru="Ляган",
            name_en="Large Plate",
            description="Qo'lda ishlangan lag'an",
            description_ru="Ручная работа",
            description_en="Handmade plate",
            price=150000,
        )
        ProductImage.objects.create(
            product=self.active_product,
            image=SimpleUploadedFile("lagan.jpg", b"file_content", content_type="image/jpeg"),
        )
        self.inactive_product = Product.objects.create(
            name="Choynak",
            name_ru="Чайник",
            name_en="Teapot",
            description="Sopol choynak",
            description_ru="Керамический чайник",
            description_en="Ceramic teapot",
            price=90000,
            is_active=False,
        )

    def test_list_returns_only_active_products(self):
        url = reverse('product-list')

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], self.active_product.id)
        self.assertIn('images', response.data[0])
        self.assertEqual(len(response.data[0]['images']), 1)
        self.assertEqual(response.data[0]['name'], self.active_product.name)
        self.assertEqual(response.data[0]['name_ru'], self.active_product.name_ru)
        self.assertEqual(response.data[0]['description_en'], self.active_product.description_en)

    def test_detail_returns_single_active_product(self):
        url = reverse('product-detail', kwargs={'pk': self.active_product.pk})

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.active_product.id)
        self.assertEqual(response.data['name'], self.active_product.name)
        self.assertEqual(response.data['name_en'], self.active_product.name_en)
        self.assertEqual(response.data['description'], self.active_product.description)
        self.assertEqual(response.data['description_ru'], self.active_product.description_ru)
        self.assertEqual(len(response.data['images']), 1)

    def test_detail_not_found_for_inactive_product(self):
        url = reverse('product-detail', kwargs={'pk': self.inactive_product.pk})

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

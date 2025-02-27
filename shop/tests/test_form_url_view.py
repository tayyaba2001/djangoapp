from django.test import TestCase
from shop.forms import ProductForm
from shop.models import Product
from django.core.files.uploadedfile import SimpleUploadedFile


class ProductFormTest(TestCase):

    def test_product_form_missing_data(self):
        """Test if ProductForm is invalid when required fields are missing."""
        form = ProductForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)
        self.assertIn('price', form.errors)
        self.assertIn('stock_quantity', form.errors)
        print("Test Product form missing data")
        
    def test_product_form_invalid_price(self):
        """Test if ProductForm catches invalid price values."""
        form = ProductForm(data={
            'name': 'Invalid Product',
            'description': 'Bad price test',
            'price': 'invalid',  # Invalid price format
            'stock_quantity': 5
        })
        
        self.assertFalse(form.is_valid())
        self.assertIn('price', form.errors)
        print("Test Product form invalid price")

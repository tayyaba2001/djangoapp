from django.test import TestCase
from django.urls import reverse
from shop.models import Product




class ProductEditTest(TestCase):
    def setUp(self):
        """Create a product for editing"""
        self.product = Product.objects.create(
            name="Laptop",
            price=99.99,
            stock_quantity=10
        )

    def test_edit_product(self):
        """Test editing a product"""
        response = self.client.post(reverse('product_update', args=[self.product.id]), {
            'name': 'Gaming Laptop',
            'description': 'Updated description', # required without aany of these field test fails
            'price': 150.00,
            'stock_quantity': 5
        })
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, "Gaming Laptop")  # Name should be updated
        self.assertEqual(float(self.product.price), 150.00)  # Price should be updated
        print("Product edit test passed!")

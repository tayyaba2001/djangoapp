from django.test import TestCase
from django.urls import reverse
from shop.models import Product




class ProductDeleteTest(TestCase):
    def setUp(self):
        """Create a product for deletion"""
        self.product = Product.objects.create(
            name="Laptop",
            price=99.99,
            stock_quantity=10
        )

    def test_delete_product(self):
        """Test deleting a product"""
        response = self.client.post(reverse('product_delete', args=[self.product.id]))
        self.assertEqual(response.status_code, 302)  # Redirect after delete
        self.assertFalse(Product.objects.filter(id=self.product.id).exists())
        print("Product delete test passed!")


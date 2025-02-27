from django.test import TestCase
from django.urls import reverse
from shop.models import Product

#    python manage.py test shop.testsmany    test-create.py
class ProductViewTest(TestCase):
    def setUp(self):
        """Set up a test product"""
        self.product = Product.objects.create(
            name="Laptop",
            price=99.99,
            stock_quantity=10
        )

    def test_view_product_list(self):
        """Test if the product list view works"""
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Laptop")  # Ensure product name is displayed
        print("Product view list passed!")

    def test_view_product_detail(self):
        """Test if the product detail page loads"""
        response = self.client.get(reverse('product_detail', args=[self.product.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Laptop")  # Ensure correct product is shown
        print("Product view detail passed!")


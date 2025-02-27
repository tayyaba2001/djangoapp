from django.test import TestCase
from shop.models import Product
class ProductModelTest(TestCase):
    def setUp(self):
        Product.objects.create(
            name="laptop",  
            price=99.99,
            stock_quantity=10  
        )

    def test_product_creation(self):
        product = Product.objects.get(name="laptop")  # Name must match
        self.assertEqual(float(product.price), 99.99)  # Convert Decimal to float
        print("Product creation test passed!")

    def test_product_in_stock(self):
        product = Product.objects.get(name="laptop")
        self.assertTrue(product.is_in_stock())  # Product should be in stock
        print("Product in stock test passed!")
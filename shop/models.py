from django import forms
# from shop.models import Product  # ✅ Import explicitly from the app


import base64
from django.db import models
from django.core.files.base import ContentFile


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField(default=0)
    image = models.BinaryField(null=True,blank=True,editable=True) #  # Store images as binary  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def set_image_from_upload(self, file_data):
        """Sets the image from an uploaded file."""
        if file_data:
            self.image = file_data.read()

    def get_base64_image(self):
        """Convert binary image data to Base64 for rendering in HTML."""
        if self.image:
            return f"data:image/png;base64,{base64.b64encode(self.image).decode('utf-8')}"
        return None
    def is_in_stock(self):
        """Returns True if the product is in stock"""
        return self.stock_quantity > 0
    def __str__(self):
        return self.name

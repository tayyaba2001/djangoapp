from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    image = forms.ImageField(required=False)  # Allow optional image uploads

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock_quantity', 'image']
    widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={ 'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock_quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.cleaned_data.get('image'):
            instance.image = self.cleaned_data['image'].read() # Convert to binary
        if commit:
            instance.save()
        return instance


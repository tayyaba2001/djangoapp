from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm

def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)  # Handle file uploads
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect after successful upload
    else:
        form = ProductForm()
    return render(request, 'shop/product_form.html', {'form': form})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'shop/product_detail.html', {'product': product})


def product_list(request):
    """View to display the list of products."""
    products = Product.objects.all()  # Fetch all products
    return render(request, 'shop/product_list.html', {'products': products})



def product_update(request, product_id):
    """View to edit an existing product."""
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'shop/product_form.html', {'form': form, 'product': product})

def product_delete(request, product_id):
    """View to delete a product."""
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == "POST":
        product.delete()
        return redirect('product_list')

    return render(request, 'shop/product_confirm_delete.html', {'product': product})

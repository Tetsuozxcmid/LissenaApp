from django.shortcuts import render,get_object_or_404
from .models import Product

# Create your views here.

def auth_home(request):
    
    products = Product.objects.filter(priceafterdiscount__isnull=False)


    return render(request, 'core/index.html', {'products': products})


def category_view(request,category_post):
    products = Product.objects.filter(category=category_post)
    category_name = dict(Product.CATEGORY_CHOICES).get(category_post, "Категория")

    return render(request, 'core/categories.html', {
        'products': products,
        'category_name': category_name,
        'category_slug': category_post
    })

def product_detail(request,post_id):
    product = get_object_or_404(Product,id=post_id)
    return render(request,'core/product.html',{'product' : product})
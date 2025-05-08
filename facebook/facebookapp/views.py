from django.shortcuts import render, get_object_or_404
from .models import Product, UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def product_list(request):
    """View to list all products."""
    products = Product.objects.all() # select * from product
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, pk):
    """View to display details of a specific product."""
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def user_profile(request, username):
    """View to display a user's profile."""
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(UserProfile, user=user)
    return render(request, 'facebookapp/user_profile.html', {'profile': profile})

@login_required
def user_profile_edit(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    return render(request, 'facebookapp/user_profile.html', {'profile': profile})
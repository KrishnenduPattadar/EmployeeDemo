from django.urls import path
from . import views

urlpatterns = [
    # Product-related views
    path('', views.product_list, name='product_list'),  # Home page lists all products
    path('product/<int:pk>/', views.product_detail, name='product_detail'),  # Product detail view

    # User profile-related views
    path('user_profile/<str:username>/', views.user_profile, name='user_profile'),  # User profile view by username
    path('user_profile/', views.user_profile_edit, name='user_profile_edit'),  # Edit logged-in user's profile
]

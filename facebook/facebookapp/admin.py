from django.contrib import admin
from .models import UserProfile, Product

# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')

admin.site.register(Product)





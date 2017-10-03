from django.contrib import admin
from .models import UserProfile
# Register your models here.
@admin.register(UserProfile)
class AdminUserProfile(admin.ModelAdmin):
    list_display = ('address', )

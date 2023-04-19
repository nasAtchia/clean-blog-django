from django.contrib import admin
from .models import User
from .models_admin import CustomUserAdmin

admin.site.register(User, CustomUserAdmin)

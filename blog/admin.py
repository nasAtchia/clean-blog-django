from django.contrib import admin

from .models import Category, Tag
from .models_admin import CategoryAdmin, TagAdmin

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)

from django.contrib import admin

from .models import Category, Post, Tag
from .models_admin import CategoryAdmin, PostAdmin, TagAdmin

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)

from django.contrib import admin


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at',)
    list_filter = ('created_at',)
    ordering = ('name',)
    prepopulated_fields = {'slug': ['name']}
    search_fields = ('name',)

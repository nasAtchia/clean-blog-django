from django.contrib import admin
from django.utils.translation import gettext_lazy as _


@admin.action(description=_('Mark posts as active'))
def make_active(modeladmin, request, queryset):
    queryset.update(status=True)


@admin.action(description=_('Mark posts as inactive'))
def make_inactive(modeladmin, request, queryset):
    queryset.update(status=False)


class PostAdmin(admin.ModelAdmin):
    actions = (make_active, make_inactive)
    exclude = ('created_by', 'updated_by',)
    list_display = ('title', 'status', 'created_by', 'updated_by', 'created_at', 'updated_at',)
    list_filter = ('created_at', 'status',)
    prepopulated_fields = {'slug': ['title'], }
    readonly_fields = ('background_image_tag',)
    search_fields = ('title',)

    def get_queryset(self, request):
        query_set = super(PostAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return query_set
        else:  # Restrict posts list to authors' own posts for the author group.
            return query_set.filter(created_by=request.user.id)

    # Auto save for created_by and updated_by field.
    def save_model(self, request, obj, form, change):
        if obj.pk is None:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)

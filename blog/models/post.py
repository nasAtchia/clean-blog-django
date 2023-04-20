from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from .category import Category
from .tag import Tag


class Post(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    body = RichTextUploadingField()
    slug = models.SlugField(unique=True, max_length=255)
    background_image = models.ImageField(upload_to='posts/')
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)
    status = models.BooleanField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
                                   related_name='%(class)s_created_by')
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
                                   related_name='%(class)s_updated_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def background_image_tag(self):
        return mark_safe(
            '<a href="%s" target="_blank"><img src="/media/%s" width="150" /></a>'
            % (self.background_image.url, self.background_image)
        )

    background_image_tag.short_description = _('Background Image')

    def __str__(self):
        return self.title

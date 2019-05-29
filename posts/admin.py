from django.contrib import admin
from . import models

@admin.register(models.Post)
class ImageAdmin(admin.ModelAdmin):
    list_diaply_links = (
    )

    search_fields = (
        'title',
    )
    
    list_filter = (
        'user',
    )

    list_display = (
        'image',
        'title',
        'user',
        'view_count',
        'created_at',
        'updated_at',
    )


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'message',
        'user',
        'post',
        'created_at',
        'updated_at',
    )
from django.contrib import admin
from src.comments.models import Comment


class CommentsAdmin(admin.ModelAdmin):
    list_display = ['user', 'content_object', 'timestamp', 'aprovado']


admin.site.register(Comment, CommentsAdmin)
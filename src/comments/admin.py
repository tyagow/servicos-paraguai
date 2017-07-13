from django.contrib import admin
from src.comments.models import Comment


class CommentsAdmin(admin.ModelAdmin):
    list_display = ['user', 'timestamp', 'aprovado']


admin.site.register(Comment, CommentsAdmin)
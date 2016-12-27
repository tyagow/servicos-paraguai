from django.contrib import admin
from src.comments.models import Comment


class CommentsAdmin(admin.ModelAdmin):
    list_display = ['nome', 'timestamp', 'aprovado']


admin.site.register(Comment, CommentsAdmin)
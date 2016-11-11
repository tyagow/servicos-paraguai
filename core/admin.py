from django.contrib import admin
from core.models import Store, Category


class StoreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'phone', 'website', 'category', 'plan']


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Store, StoreAdmin)
admin.site.register(Category, CategoryAdmin)

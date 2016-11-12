from django.contrib import admin
from core.models import Store, Category, Advertisement


class StoreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'phone', 'website', 'category', 'plan']


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['store', 'expires_at', 'photo_img', 'kind']

    def photo_img(self, obj):
        return '<img width="42px" height="32px" src="{}" />'.format(obj.img)

    photo_img.allow_tags = True
    photo_img.short_description = "Anúncio"

admin.site.register(Store, StoreAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Advertisement, AdvertisementAdmin)

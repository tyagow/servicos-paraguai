from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from src.accounts.models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, )

# Re-register UserAdmin
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'status']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        instance = super(ProfileForm, self).save()
        return instance


class ProfileAdmin(admin.ModelAdmin):
    form = ProfileForm
    list_display = ['user', 'status', 'email']
    list_filter = ['status']
    ordering = ['status']

    def email(self, obj):
        return obj.user.email if obj.user.email else 'Não Cadastrado'


admin.site.register(Profile, ProfileAdmin)
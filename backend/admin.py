from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms
from models import *

class GetInUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class GetInUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User


    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])


class GetInUserAdmin(UserAdmin):
    form = GetInUserChangeForm
    add_form = GetInUserCreationForm
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('type',)}),
    )

admin.site.register(User, GetInUserAdmin)


# admin.site.register(User, UserAdmin)
admin.site.register(PregnantGirl)
admin.site.register(AntenatalVist)
admin.site.register(PresetMessage)

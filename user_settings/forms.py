from django import forms
from django.contrib.auth.forms import PasswordChangeForm

from .models import *
from django.forms import ModelForm

class ApplicationSettingForm(ModelForm):
    class Meta:
        model = UserSetting
        fields = [
            'number_of_questions',
            'default_game_query',
            ]
        help_texts = {
            'number_of_questions': 'Number of questions in one game',
            'default_game_query': 'Query for filtering cards based on tags',
        }

class UserEditForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            ]


class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(user, *args, **kwargs)

    def save(self, commit=True):
        password = self.cleaned_data["new_password1"]
        self.user.set_password(password)
        if commit:
            self.user.save()
        return self.user
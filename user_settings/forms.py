from django import forms
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
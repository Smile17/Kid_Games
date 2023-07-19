from django import forms
from .models import *
from django.forms import ModelForm

# Sign Up Form
class ApplicationSettingForm(ModelForm):
    class Meta:
        model = UserSettings
        fields = [
            'autoplay_sound',
            'number_of_questions'
            ]
        help_texts = {
            'autoplay_sound': 'Autoplay sound on web pages',
            'number_of_questions': 'Number of questions in one game'
        }
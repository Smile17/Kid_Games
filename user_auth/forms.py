from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Sign Up Form
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            ]
        help_texts = {
            'username': None,
            'password1': None,
            'password2': None,
        }
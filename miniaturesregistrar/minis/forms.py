from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from minis.models import Army, System, Miniature


class AddMiniForm(forms.Form):
    system = forms.ModelChoiceField(queryset=System.objects.all(),
                                           required=True, empty_label="----")
    army = forms.ModelChoiceField(queryset=Army.objects.all(),
                                         required=True, empty_label="----",)
    name = forms.CharField(max_length=128, required=True)

def validate_username(value):
    if User.objects.filter(username=value).exists():
        raise ValidationError('Username already exists!')


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=16, required=True, validators=[validate_username])
    email = forms.EmailField(required=True)
    password = forms.CharField(max_length=128, required=True, widget=forms.PasswordInput)

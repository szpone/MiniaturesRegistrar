from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from minis.models import Army, System, Miniature


class AddMiniForm(forms.Form):
    system_choice = forms.ModelChoiceField(queryset=System.objects.all(),
                                           required=True, empty_label="----")
    army_choice = forms.ModelChoiceField(queryset=Army.objects.all(),
                                         required=True, empty_label="----",)
    miniature_choice = forms.ModelChoiceField(
                                            queryset=Miniature.objects.all(),
                                            required=True, empty_label="----")

def validate_username(value):
    if User.objects.filter(username=value).exists():
        raise ValidationError('Username already exists!')


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=16, required=True, validators=[validate_username])
    email = forms.EmailField(required=True)
    password = forms.CharField(max_length=128, required=True, widget=forms.PasswordInput)



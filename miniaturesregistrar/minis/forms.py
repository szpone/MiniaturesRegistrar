from django import forms
from minis.models import Army, System, Miniature, PaintManufacturer, Paint


class AddMiniForm(forms.Form):
    army_choice = forms.ModelChoiceField(queryset=Army.objects.all(),
                                         required=True, empty_label="----",)
    system_choice = forms.ModelChoiceField(queryset=System.objects.all(),
                                           required=True, empty_label="----")
    miniature_choice = forms.ModelChoiceField(
                                            queryset=Miniature.objects.all(),
                                            required=True, empty_label="----")

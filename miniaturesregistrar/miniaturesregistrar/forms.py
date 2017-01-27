from django import forms
from minis.models import Army, System, Miniatures, PaintManufacturer, Colors


class AddMini(forms.Form):
    army_choice = forms.ModelChoiceField(queryset=Army.objects.all(),
                                         required=True, empty_label="----",)
    system_choice = forms.ModelChoiceField(queryset=System.objects.all(),
                                           required=True, empty_label="----")
    miniature_choice = forms.ModelChoiceField(
                                            queryset=Miniatures.objects.all(),
                                            required=True, empty_label="----")

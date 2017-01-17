from django.shortcuts import render
from django.views.generic import FormView
from minis.forms import AddMini
from django.views import View
from minis.models import Miniature
# Create your views here.


class AddMiniForm(FormView):
    template_name = 'minis/addmini_form.html'
    form_class = AddMini

    def form_valid(self, form):
        d = dict()
        d['army_choice'] = form.cleaned_data['army_choice']
        d['system_choice'] = form.cleaned_data['system_choice']
        d['miniature_choice'] = form.cleaned_data['miniature_choice']
        return render(None, 'minis/addmini_form.html', {"data": d})


class MiniColors(View):
    def get(self, request):
        form = AddMini
        return render(request, 'minis/addmini_form.html', {"form": form})

    def post(self, request):
        pass

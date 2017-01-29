
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect, Http404
from django.views import View
from django.views.generic import FormView
from minis.forms import AddMiniForm, RegistrationForm
from minis.models import Miniature, Paint, PaintManufacturer, MINIATURE_ELEMENTS, Element, System
from rest_framework.response import Response
from rest_framework.views import APIView
import json


# Create your views here.


class AddMiniView(LoginRequiredMixin, FormView):
    template_name = 'minis/addmini_form.html'
    form_class = AddMiniForm

    def form_valid(self, form):
        army = form.cleaned_data['army']
        name = form.cleaned_data['name']
        user = self.request.user
        if 'image' in self.request.FILES:
            image = self.request.FILES['image']
        else:
            image = None
        miniature = Miniature.objects.create(army=army, name=name,
                                             user=user, mini_image=image)
        return redirect("mini-colors", miniature.id)


class MiniColorsView(LoginRequiredMixin, View):
    def get(self, request, miniature_id):
        miniature = get_object_or_404(Miniature, pk=miniature_id,
                                      user=request.user)
        manufacturers = PaintManufacturer.objects.all()
        element_types = MINIATURE_ELEMENTS
        elements = Miniature.objects.get(pk=miniature_id).elements

        # list of [el_type_id, el_type_name, paints]
        el_types = []
        for el_type_id, el_type_name in element_types:
            elements_of_this_type = elements.filter(number=el_type_id)

            if elements_of_this_type.count() > 0:
                element = elements_of_this_type[0]
                all_paints = element.paints.all()

                paints = [
                    all_paints[0] if all_paints.count() > 0 else None,
                    all_paints[1] if all_paints.count() > 1 else None,
                    all_paints[2] if all_paints.count() > 2 else None,
                ]
            else:
                paints = [None, None, None]

            el_types.append([el_type_id, el_type_name, paints])

        for m in manufacturers:
            m.paints = m.paint_set.all()

        return render(request, 'minis/mini_colors.html', {
            'miniature': miniature,
            'manufacturers': manufacturers,
            'elements': element_types,
            'el_type': el_types,
            'paint_range': range(3),
        })


class ElementView(LoginRequiredMixin, APIView):
    def post(self, request, id, format=None):
        miniature = get_object_or_404(Miniature, pk=id, user=request.user)

        comment = request.data['comment']
        all_colors = request.data['colors']
        for index, colors in enumerate(json.loads(all_colors)):
            print(index, colors)
            element, _create = Element.objects.get_or_create(
                number=index, miniature=miniature)
            for paint_pk in map(int, filter(lambda x: x, colors)):
                element.paints.add(Paint.objects.get(pk=paint_pk))
            element.save()

        miniature.comment = comment
        miniature.save()

        return Response('OK')


class MainView(LoginRequiredMixin, View):
    def get(self, request):
        user_miniatures = Miniature.objects.filter(user=request.user)

        systems = System.objects.all()
        return render(request, 'minis/main_page.html', {
            'systems': systems,
            'user_miniatures': user_miniatures,
        })


class RegisterView(FormView):
    template_name = 'registration/registration_form.html'
    form_class = RegistrationForm

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        email = form.cleaned_data['email']
        User.objects.create_user(username, email, password)
        return redirect('main')

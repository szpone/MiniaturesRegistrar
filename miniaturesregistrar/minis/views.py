import json

from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import FormView
from minis.forms import AddMiniForm
from minis.models import Miniature, Paint, PaintManufacturer, MINIATURE_ELEMENTS, Element, System
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.


class AddMiniView(FormView):
    template_name = 'minis/addmini_form.html'
    form_class = AddMiniForm

    def form_valid(self, form):
        miniature = form.cleaned_data['miniature_choice']
        return redirect("mini-colors", miniature.id)


class MiniColorsView(View):
    def get(self, request, miniature_id):
        miniature = Miniature.objects.get(pk=miniature_id)
        manufacturers = PaintManufacturer.objects.all()
        element_types = MINIATURE_ELEMENTS
        elements = Miniature.objects.get(pk=miniature_id).elements
        el_type = []
        for el_type_id, name in element_types:
            el_for_types = elements.filter(number=el_type_id)
            _eee = [el_type_id,name]
            if el_for_types.count():
                el = el_for_types[0].paints.all()
                _eeee = []
                for i in range(3):
                    if i < el.count():
                        _eeee.append(el[i])
                    else:
                        _eeee.append(None)
                _eee.append(_eeee)
            else:
                _eee.append([None,None,None])
            el_type.append(_eee)

        for m in manufacturers:
            m.paints = m.paint_set.all()



        return render(request, 'minis/mini_colors.html', {
            'miniature': miniature,
            'manufacturers': manufacturers,
            'elements': element_types,
            'el_type': el_type,
            'paint_range': range(3),
        })

    def post(self, request):
        pass


class ElementView(APIView):
    def post(self, request, id, format=None):
        print(request.data)

        comment = request.data['comment']
        all_colors = request.data['colors']
        mini = Miniature.objects.get(pk=id)
        for index, colors in enumerate(json.loads(all_colors)):
            print(index, colors)
            # element = Element()
            element, _create = Element.objects.get_or_create(number=index,
                                                             miniature=mini)
            for paint_pk in map(int, filter(lambda x: x, colors)):
                element.paints.add(Paint.objects.get(pk=paint_pk))
            element.save()

        mini.comment = comment
        mini.save()

        return Response('OK')
        # fajnie byłoby usuwać kolory


class MainView(LoginRequiredMixin, View):
    def get(self, request):
        systems = System.objects.all()
        return render(request, 'minis/main_page.html', {'systems': systems})

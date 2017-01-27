from django.shortcuts import render, redirect
from django.views.generic import FormView
from minis.forms import AddMiniForm
from django.views import View
from minis.models import Miniature, Paint, PaintManufacturer, MINIATURE_ELEMENTS, Element, System
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .serializers import ElementsSerializer
from django.views.decorators.csrf import csrf_exempt
import json
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


# class ElementView(APIView):
#     def get_object(self, pk):
#         try:
#             return Element.objects.get(pk=pk)
#         except Element.DoesNotExist:
#             raise Http404

#     def get(self, request, id, format=None):
#         element = self.get_object(id)
#         serializer = ElementsSerializer(element, context={"request": request})
#         return Response(serializer.data)

#     def put(self, request, id, format=None):
#         element = self.get_object(id)
#         serializer = ElementsSerializer(element, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)


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


class MainView(View):
    def get(self, request):
        systems = System.objects.all()
        return render(request, 'minis/main_page.html', {'systems': systems})

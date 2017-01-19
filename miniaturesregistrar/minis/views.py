from django.shortcuts import render, redirect
from django.views.generic import FormView
from minis.forms import AddMiniForm
from django.views import View
from minis.models import Miniature, Paint, PaintManufacturer, MINIATURE_ELEMENTS, Element
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
        d = dict()
        d['army_choice'] = form.cleaned_data['army_choice']
        d['system_choice'] = form.cleaned_data['system_choice']
        d['miniature_choice'] = form.cleaned_data['miniature_choice']
        return redirect("mini-colors")


class MiniColorsView(View):
    def get(self, request, miniature_id):
        miniature = Miniature.objects.get(pk=miniature_id)
        manufacturers = PaintManufacturer.objects.all()
        elements = MINIATURE_ELEMENTS
        elements_e = []


        for m in manufacturers:
            m.paints = m.paint_set.all()



        return render(request, 'minis/mini_colors.html', {
            'miniature': miniature,
            'manufacturers': manufacturers,
            'elements': elements,
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
        all_colors = request.data['colors']
        for index, colors in enumerate(json.loads(all_colors)):
            print(index, colors)
            # element = Element()
            min_id = Miniature.objects.get(pk=id)
            element, _create = Element.objects.get_or_create(number=index,
                                                             miniature=min_id)
            element.save()
            for paint_pk in map(int, filter(lambda x: x, colors)):
                element.paints.add(Paint.objects.get(pk=paint_pk))
            element.save()

        print(request.data)
        return Response('OK')
        # fajnie byłoby usuwać kolory

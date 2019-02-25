from django.shortcuts import render
from django.template import Template
from django.template.response import TemplateResponse, HttpResponse
from django.template.loader import render_to_string

from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, CreateView, UpdateView, View

from django.urls import reverse

from django.template import RequestContext
from django.shortcuts import render, render_to_response

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
import googlemaps
# Create your views here.

class Home(View):
    template_name = 'home_temp/about.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)	

home = Home.as_view()

@method_decorator(csrf_exempt)
def Showcar(request, *args, ** kwargs):
    template_name =''
    print(request.POST)
    cars_det = json.loads(request.body)

    gmaps = googlemaps.Client(key='AIzaSyAwS1dG9Y5vT_F3jcul4d2C69nRsroOVOE')
    local = gmaps.distance_matrix(cars_det["from"], cars_det['to'])
    print(json.dumps(local, indent=4, sort_keys=True))
    if not local['rows'][0]['elements'][0]['status'] =="NOT_FOUND":
        int_dis=local['rows'][0]['elements'][0]['distance']['text']
    else:
        print("route not found")

    distance = int_dis.replace(' km','')

    distance=distance.replace(',','')
    distance = float(distance)
    round_trip=float(distance)*2
    seater=int(cars_det['seat'])
    sdata={'seat':int(cars_det['seat']),'duration':int(cars_det['duration']),'distance':distance,'round_trip':round_trip}
    if seater==4:
        data={}
        data['status']=1
        data['html'] = render_to_string('home_temp/4seater.html', sdata)
    elif seater == 6:
        data = {}
        data['status'] = 1
        data['html'] = render_to_string('home_temp/6seater.html', sdata)
    elif seater == 7:
        data = {}
        data['status'] = 1
        data['html'] = render_to_string('home_temp/7seater.html', sdata)
    elif seater==11:
        data = {}
        data['status'] = 1
        data['html'] = render_to_string('home_temp/11seater.html', sdata)

    return HttpResponse(json.dumps(data), content_type='application/x-json')


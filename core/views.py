from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
import core.models as coremodels

class LandingView(TemplateView):
    template_name = "base/index.html"

class LocationListView(ListView):
    model = coremodels.Location
    template_name = "location/list.html"
#    template_name = 'base/theme.html' if you want to take a look

class LocationDetailView(DetailView):
    model = coremodels.Location
    template_name = "location/detail.html"
    context_object_name = 'location'


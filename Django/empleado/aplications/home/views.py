from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
# Create your views here.
from .models import Prueba

from .forms import PruebaForm

class IndexView(TemplateView):
    template_name = 'home/home.html'


class ResumenFoundationView(TemplateView):
    template_name = "home/resume_foundation.html"
    

class PruebaListView(ListView):
        template_name = 'home/lista.html'
        queryset = ['A','B','C']
        context_object_name = 'lista_prueba'


class ModeloPruebaListView(ListView):
    model = Prueba
    template_name = "home/pruebas.html"
    context_object_name='lista_prueba'


class PruebaCreateView(CreateView):
    model = Prueba
    template_name = "home/add.html"
    form_class= PruebaForm
    #fields=['titulo','subtitulo','catidad']
    success_url='/'
    
        
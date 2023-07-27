from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
    
)

from aplications import persona
#models
from .models import Empleado
#forms
from .forms import EmpleadoForm


class InicioView(TemplateView):
    """Vista que carga la pagina de inicio"""
    template_name = "inicio.html"


class ListAllEmpleados(ListView):
    template_name='persona/list_all.html'
    paginate_by= 4
    ordering='first_name'
    #model= Empleado
    context_object_name= 'empleados'
    def get_queryset(self):
        palabra_clave= self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            full_name__icontains=palabra_clave 
            #busca cadenas con similitudes (jo) lista todo lo que tenga dentro de la cadena jo
        )  
        return lista


class ListaEmpleadosAdmin(ListView):
    template_name='persona/lista_empleados.html'
    paginate_by= 10
    ordering='first_name'
    model= Empleado
    context_object_name= 'empleados'
       


class ListByArea(ListView):
    #lista empleados de un area
    template_name='persona/list_by_area.html'
    context_object_name='empleados'
   
    def get_queryset(self):
        area= self.kwargs['shorname']
        lista = Empleado.objects.filter(
            departamento__shor_name=area
        )
        return lista

class ListEmpleadosByKword(ListView):
        #Lista por palabra clave
        template_name = 'persona/by_kword.html'
        context_object_name= 'empleados'
        
        def get_queryset(self):
            print('***************************')
            palabra_clave= self.request.GET.get("kword", '')
            lista = Empleado.objects.filter(
            first_name=palabra_clave
        )
           
            return lista
        
class ListHabilidadesEmpleado(ListView):
     template_name= 'persona/habilidades.html'
     context_object_name= 'habilidades'
     def get_queryset(self):
        empleado= Empleado.objects.get(id=7)
        return empleado.habilidades.all()
     

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"
 
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo']= "empleado del mes"
        return context


class SuccesView(TemplateView):
    template_name = "persona/succes.html"


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add.html"
    form_class=EmpleadoForm
    #fields=['first_name','last_name','job']
    #fields=('__all__')#carga todos los campos del modelo
    """fields=[
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
        'avatar'

    ] ya no porque se va a utilizar el form"""
    #success_url= '.'#para que se recargue la misma pagina
    success_url= reverse_lazy('persona_app:empleados_admin')

    def form_valid(self, form):
        #logica del proceso
        empleado=form.save()
        empleado.full_name = empleado.first_name+ ' '+empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)
            


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/update.html"
    fields=[
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades'

    ]
    success_url= reverse_lazy('persona_app:empleados_admin')

    def post(self, request, *args, **kwargs):
        #obtengo los datos de los campos
        self.object= self.get_object()
        print('****************METODO POST**************')
        print('****************************')
        print('========')
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        #logica del proceso
        print('****************METODO form valid**************')
        print('****************************')
        return super(EmpleadoUpdateView, self).form_valid(form)


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url= reverse_lazy('persona_app:empleados_admin')
             
from django.shortcuts import render, redirect

# Create your views here.
from ordenamiento.models import *
from ordenamiento.forms import *

# Generar una vista que liste las parroquias y sus barrios
def index(request):
    parroquias = Parroquia.objects.all()

    informacion_template = {'parroquias': parroquias, 'numero_parroquias':len(parroquias)}
    return render(request, 'index.html', informacion_template)
    
def obtener_parroquia(request, id):

    parroquia = Parroquia.objects.get(pk=id)

    informacion_template = {'parroquia': parroquia}
    return render(request, 'obtener_parroquia.html', informacion_template)

# Generar una vista que liste los barrios
def obtener_barrio(request):

    barrios = Barrio.objects.all()

    informacion_template = {'barrios': barrios}
    return render(request, 'barrios.html', informacion_template)

# Generar un formulario que cree una parroquia
def crear_parroquia(request):

    if request.method=='POST':
        formulario = ParroquiaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() # se guarda en la base de datos
            return redirect(index)
    else:
        formulario = ParroquiaForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearParroquia.html', diccionario)

# Generar un formulario que cree un barrio de una parroquia
def crear_barrio_parroquia (request, id):

    parroquia = Parroquia.objects.get(pk=id)
    if request.method=='POST':
        formulario = BarrioParroquiaForm(parroquia, request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioParroquiaForm(parroquia)
    diccionario = {'formulario': formulario, 'parroquia': parroquia}

    return render(request, 'crearBarrioParroquia.html', diccionario)

# Generar un formulario que edite una parroquia
def editar_parroquia(request, id):
    parroquia = Parroquia.objects.get(pk=id)
    if request.method=='POST':
        formulario = ParroquiaForm(request.POST, instance=parroquia)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ParroquiaForm(instance=parroquia)
    diccionario = {'formulario': formulario}

    return render(request, 'editarParroquia.html', diccionario)

# Generar un formulario que edite un barrio
def editar_barrio(request, id):
    barrio = Barrio.objects.get(pk=id)
    if request.method=='POST':
        formulario = BarrioForm(request.POST, instance=barrio)
        (formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioForm(instance=barrio)
    diccionario = {'formulario': formulario}

    return render(request, 'editarBarrio.html', diccionario)
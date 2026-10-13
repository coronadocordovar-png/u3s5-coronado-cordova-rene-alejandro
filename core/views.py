from django.shortcuts import render
from django.db import connection
from .models import Servicio


def inicio(request):
    info_bd = connection.settings_dict

    contexto = {
        'motor': info_bd['ENGINE'],
        'host': info_bd['HOST'],
    }

    return render(request, 'core/inicio.html', contexto)


def servicios(request):
    servicios = Servicio.objects.order_by('-creado_en')

    contexto = {
        'servicios': servicios
    }

    return render(request, 'core/servicios.html', contexto)


def contacto(request):
    return render(request, 'core/contacto.html')


from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from .forms import ServicioForm


@login_required
def crear_servicio(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            nuevo = form.save(commit=False)
            nuevo.propietario = request.user
            nuevo.save()
            return redirect('servicios')
    else:
        form = ServicioForm()
    return render(request, 'core/servicio_form.html', {'form': form, 'titulo': 'Crear servicio'})


@login_required
def editar_servicio(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk, propietario=request.user)
    if request.method == 'POST':
        form = ServicioForm(request.POST, instance=servicio)
        if form.is_valid():
            form.save()
            return redirect('servicios')
    else:
        form = ServicioForm(instance=servicio)
    return render(request, 'core/servicio_form.html', {'form': form, 'titulo': 'Editar servicio'})


@login_required
def eliminar_servicio(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk, propietario=request.user)
    if request.method == 'POST':
        servicio.delete()
        return redirect('servicios')
    return render(request, 'core/servicio_confirm_delete.html', {'servicio': servicio})


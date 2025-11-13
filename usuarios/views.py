from django.shortcuts import render
from django.shortcuts import redirect

def home(request):
    return render(request, 'usuarios/index.html')


def productos(request):
    return redirect('productos')  # redirige al CRUD de productos

def ventas(request):
    return render(request, 'usuarios/ventas.html')

def clientes(request):
    return render(request, 'usuarios/clientes.html')

def reportes(request):
    return render(request, 'usuarios/reportes.html')

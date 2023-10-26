from django.shortcuts import render, redirect
from .models import *
import os
from django.conf import settings
from django.http import HttpResponse
import json
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import IntegrityError
from django.contrib import messages
# Create your views here.


def cargarInicio(request):
    productos = Producto.objects.all()
    categoria_perros = Producto.objects.filter(id_categoria = 1)
    categoria_gatos = Producto.objects.filter(id_categoria = 2)
    return render(request,"Inicio.html",{"prod":productos,"cate_gatos":categoria_gatos,"cate_perros":categoria_perros})
    


def cargarAgregarProducto(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    return render(request,"agregarProducto.html",{"cate":categorias, "prod":productos})


def agregarProducto(request):
    #print("PRODUCTO AGREGAR", request.POST)

    v_sku = request.POST['txtSku']
    v_nombre = request.POST['txtNombre']
    v_stock = request.POST['txtStock']
    v_precio = request.POST['txtPrecio']
    v_descripcion = request.POST['txtDescripcion']
    v_img = request.FILES['txtImg']
    v_categoria = Categoria.objects.get(id_categoria = request.POST['cmbCategoria'])

    try: 


        Producto.objects.create(sku = v_sku,nombre = v_nombre,stock = v_stock,precio = v_precio,descripcion = v_descripcion, id_categoria = v_categoria, imagen_url = v_img)        
    except IntegrityError:
        messages.error(request, 'El SKU ya existe. Elija otro SKU.')
        return redirect('/agregarProducto')
    return redirect('/agregarProducto')



def cargarEditarProducto(request,sku):
    productos = Producto.objects.get(sku = sku)
    categorias = Categoria.objects.all()
    return render(request,"editarProducto.html",{"prod":productos,"cate":categorias})

def editarProducto(request):
    v_sku = request.POST['txtSku']
    productoBD = Producto.objects.get(sku = v_sku)
    v_nombre = request.POST['txtNombre']
    v_stock = request.POST['txtStock']
    v_precio = request.POST['txtPrecio']
    v_descripcion = request.POST['txtDescripcion']
    v_categoria = Categoria.objects.get(id_categoria = request.POST['cmbCategoria'])

    try:
        v_img = request.FILES['txtImg']
        ruta_imagen = os.path.join(settings.MEDIA_ROOT, str(productoBD.imagen_url))
        os.remove(ruta_imagen)
    except:
        v_img = productoBD.imagen_url


    productoBD.nombre = v_nombre
    productoBD.stock = v_stock
    productoBD.precio = v_precio
    productoBD.descripcion = v_descripcion
    productoBD.imagen_url = v_img
    productoBD.id_categoria = v_categoria

    productoBD.save()


    return redirect('/agregarProducto')


def eliminarProducto(request,sku):
    producto = Producto.objects.get(sku = sku)
    ruta_imagen = os.path.join(settings.MEDIA_ROOT, str(producto.imagen_url))
    os.remove(ruta_imagen)
    producto.delete()
    return redirect('/agregarProducto')


def carrito(request):
    #print("CARRITO",request.body)

    productos = json.loads(request.body)

    for p in productos:
        print("SKU",p['sku'])
        print("CANTIDAD",p['cantidad'])

    return HttpResponse("Ok!")


def contactanos(request):
    return render(request,"contactanos.html")


def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html',{
        'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST
            ['password'])
        if user is None:
            return render(request, 'signin.html',{
                'form': AuthenticationForm,
                'error': 'El usuario o la contraseña es incorrecta'
            })
        else:
            login(request, user)
            return redirect('home')


def signup(request):

    if request.method == 'GET':
        return render(request,"signup.html",{
        'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # register user
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user) #cookies
                return redirect('home')
            except:
                return render(request,"signup.html",{
                    'form': UserCreationForm,
                    "error": 'Usuario ya existe'
                })   
        return render(request,"signup.html",{
            'form': UserCreationForm,
            "error": 'Contraseñas no coinciden'
        })   






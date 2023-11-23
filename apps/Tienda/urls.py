from django.urls import path
from . import views


urlpatterns = [
    path('',views.cargarInicio, name='home'),
    path('agregarProductoForm',views.agregarProducto),
    path('editarProducto/<sku>',views.cargarEditarProducto),
    path('editarProductoForm',views.editarProducto),
    path('eliminarProducto/<sku>',views.eliminarProducto),
    path('carrito',views.carrito),
    path('contactanos',views.contactanos),
    path('signup/', views.signup, name='signup'),
    path('agregarProducto/', views.cargarAgregarProducto, name='cargarAgregarProducto'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin')
]
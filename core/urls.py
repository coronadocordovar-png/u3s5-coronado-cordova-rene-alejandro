# path: funciÃ³n para definir una ruta individual
from django.urls import path

# views: importa las vistas de esta misma app
from . import views

# Lista de rutas de la app core
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('servicios/', views.servicios, name='servicios'),
    path('contacto/', views.contacto, name='contacto'),
    path('servicios/nuevo/', views.crear_servicio, name='crear_servicio'),
    path('servicios/<int:pk>/editar/', views.editar_servicio, name='editar_servicio'),
    path('servicios/<int:pk>/eliminar/', views.eliminar_servicio, name='eliminar_servicio'),
]

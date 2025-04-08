from django.urls import path
from . import views

urlpatterns = [
    path('', views.nombre_en_la_web, name='nombre_en_la_web'),
    path('mi_tarjeta/', views.mi_tarjeta_web, name='mi_tarjeta_web'),
    path('saludo/<str:nombre>/', views.saludo, name='saludo'),
]

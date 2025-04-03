from django.shortcuts import render

def nombre_en_la_web(request):
    return render(request, 'nombre_en_la_web.html')

def mi_tarjeta_web(request):
    return render(request, 'mi_tarjeta_web.html')



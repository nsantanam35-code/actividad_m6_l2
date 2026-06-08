from django.urls import path
from django.http import HttpResponse

def index(request):
    return HttpResponse("¡Bienvenido a mi sitio!")

urlpatterns = [
    path('', index),
]

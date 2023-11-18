"""
URL configuration for crear_perfil project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from perfil import views
from perfil.views import crear_alumno, perfil_alumno



urlpatterns = [
    path('admin/', admin.site.urls),
    path('perfil/profesor/crear/', views.crear_profesor, name='crear_profesor'),
    path('perfil/profesor/editar/', views.editar_profesor, name='editar_profesor'),
    path('perfil/profesor/', views.perfil_profesor, name='perfil_profesor'),

    path('perfil/alumno/crear/', crear_alumno, name='crear_alumno'),
    path('perfil/alumno/', perfil_alumno, name='perfil_alumno')
]
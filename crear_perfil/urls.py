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
from django.urls import path, include
from Perfil import views
from Perfil.views import crear_perfil_profesor, perfil_profesor, crear_perfil_alumno, perfil_alumno
urlpatterns = [
    path('admin/', admin.site.urls),

    path('crear_perfil_profesor/', crear_perfil_profesor, name='crear_perfil_profesor'),
    path('perfil_profesor/', perfil_profesor, name='perfil_profesor'),
    path('crear_perfil_alumno/', crear_perfil_alumno, name='crear_perfil_alumno'),
    path('perfil_alumno/', perfil_alumno, name='perfil_alumno'),
]

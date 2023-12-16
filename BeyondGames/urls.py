"""
URL configuration for ProyectoFinal project.

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

from BeyondGames.views import publicacion, create_publicacion, pag_principal, BlogList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', pag_principal, name="Inicio"),
    path('accounts/', include('accounts.urls')),
    path('new_publicacion/',create_publicacion, name = 'publicar'),
    path('blog/<int:publicacion_id>/', publicacion, name = 'publicacion'),
    path('inicio/lista/', BlogList.as_view(), name="BlogLista"),
]
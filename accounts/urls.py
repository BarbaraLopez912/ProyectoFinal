from django.contrib import admin
from django.urls import path

from accounts.views import registro

urlpatterns = [
    path('registro/', registro, name="Registro"),
    path('admin/', admin.site.urls),
]

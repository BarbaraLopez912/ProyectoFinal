from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path

from accounts.views import register_request, login_request, editar_request, avatar_request

urlpatterns = [
    path('registro/', register_request, name="Registro"),
    path('login/', login_request, name="Login"),
    path('logout/', LogoutView.as_view(template_name="accounts/logout.html"), name="Logout"),
    path('admin/', admin.site.urls),
    path('editar/', editar_request, name="EditarRegistro"),
    path('avatar/', avatar_request, name="Avatar"),
]

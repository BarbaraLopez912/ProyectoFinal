from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from accounts.forms import UserRegisterForm
from django.contrib import messages

def register_request(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Inicio")
        else:
            print(form.errors)
            messages.error(request, "Hubo un error en el formulario. Por favor, verifica los campos.")
    else:
        form = UserRegisterForm()

    contexto = {"form": form}
    return render(request, "accounts/registro.html", contexto)




def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            data = form.cleaned_data

            usuario = data.get('username')
            contrasenia = data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user:
                login(request, user)

        return redirect('/app/inicio/')

    form = AuthenticationForm()
    contexto = {
        "form": form
    }
    return render(request, "accounts/login.html", contexto)
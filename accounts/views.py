from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from accounts.forms import UserRegisterForm, UserUpdateForm, AvatarUpdateForm
from django.contrib import messages

from accounts.models import Avatar


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

@login_required
def editar_request(request):
    user = request.user
    if request.method == "POST":
        form = UserUpdateForm(request.POST)
        if form.is_valid():
            user.email = request.POST["email"]
            user.username = request.POST["username"]
            user.save()
            return redirect("BlogLista")

    form = UserUpdateForm(initial={"email": user.email, "username": user.username})
    contexto={
        "form": form
    }
    return render(request, "accounts/registro.html", contexto)


@login_required
def avatar_request(request):
    user = request.user
    if request.method == "POST":

        form = AvatarUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            data=form.cleaned_data

            try:
                avatar=user.avatar
                avatar.imagen = data["imagen"]
            except:
                avatar=Avatar(
                    user=user,
                    imagen=data["imagen"]
                )
            avatar.save()

            return redirect("BlogLista")
    form = AvatarUpdateForm()
    contexto={
        "form": form
    }
    return render(request, "accounts/avatar.html", contexto)


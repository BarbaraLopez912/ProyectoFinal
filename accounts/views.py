from django.shortcuts import render, redirect
from accounts.forms import UserRegisterForm


def registro(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/app/inicio/")

    form = UserRegisterForm()
    contexto={
        "form": form
    }
    return render(request, "accounts/registro.html", contexto)

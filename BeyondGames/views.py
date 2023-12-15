from django.shortcuts import render

def pag_principal(request):
    contexto={}
    return render (request, 'Base/base.html', contexto)

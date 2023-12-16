from django.shortcuts import render,redirect
from BeyondGames.forms import PublicacionForm
from BeyondGames.models import Publicacion

def pag_principal(request):
    publicaciones= Publicacion.objects.all().order_by('-create_date')
    featured_post = publicaciones.first()
    contexto = {'publicaciones':publicaciones,'featured_post': featured_post}
    return render (request, 'Base/base.html', contexto)

def create_publicacion(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Inicio')  
    else:
        form = PublicacionForm()
    return render(request,'pages/nueva_publicacion.html',{'form':form})

def publicacion(request):
    publicaciones= Publicacion.objects.all()
    contexto = {'publicaciones':publicaciones}
    return render (request, 'pages/blog.html', contexto)
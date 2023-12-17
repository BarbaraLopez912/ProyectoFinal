from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render,redirect
from BeyondGames.forms import PublicacionForm, BuscarBlog
from BeyondGames.models import Publicacion
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

def pag_principal(request):
    publicaciones= Publicacion.objects.all().order_by('-create_date')
    featured_post = publicaciones.first()
    contexto = {'publicaciones':publicaciones,'featured_post': featured_post}
    return render (request, 'Base/base.html', contexto)

@login_required
def create_publicacion(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Inicio')  
    else:
        form = PublicacionForm()
    return render(request,'pages/nueva_publicacion.html',{'form':form})

def publicacion(request, publicacion_id):
    publicacion = get_object_or_404(Publicacion, pk=publicacion_id)
    publicaciones= Publicacion.objects.all()
    contexto = {
        'publicaciones':publicaciones,
        'publicacion': publicacion
        }
    return render (request, 'pages/publicacion.html', contexto)

class BlogList(LoginRequiredMixin, ListView):
    model = Publicacion
    template_name = "BeyondGames/lista_blogs.html"

class BlogDetalle(LoginRequiredMixin, DetailView):
    model=Publicacion
    template_name="BeyondGames/detalle_blog.html"

class BlogEliminar(LoginRequiredMixin, DeleteView):
    model=Publicacion
    template_name = "BeyondGames/eliminar_blog.html"
    success_url = "/app/inicio/lista"

class BlogUpdate(LoginRequiredMixin, UpdateView):
    model = Publicacion
    success_url = "/app/inicio/lista"
    template_name = "pages/update_blog.html"
    fields=["title", "opinion", "console", "release_date", "category", "front_page"]

def sobre_nosotros(request):
    contexto={}
    return render(request, 'pages/sobre_nosotros.html', contexto)

def busqueda_blog(request):
    nombre=request.GET.get("title")
    if nombre is not None:
        publicaciones=Publicacion.objects.filter(title__icontains=nombre)
    else:
        publicaciones=[]
    contexto={
        "publicaciones": publicaciones,
        "form": BuscarBlog(initial={"title": nombre})
        }
    return render(request, "Base/base.html", contexto)

from django import forms
from .models import Publicacion

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['title', 'opinion','console', 'release_date','category','front_page']
        labels = {
            'title': 'Nombre de tu publicación',
            'opinion': 'Opinión',
            'console': 'Consola',
            'release_date': 'Fecha de lanzamiento',
            'category': 'Categoría',
            'front_page':'Portada'
        }

class BuscarBlog(forms.Form):
    title=forms.CharField()
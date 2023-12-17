from django import forms
from .models import Comentario, Publicacion

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

class ComentarioForm(forms.ModelForm):
    class Meta:
        model= Comentario
        fields = ['autor','texto']
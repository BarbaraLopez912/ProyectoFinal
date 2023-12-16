from typing import Any

from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import CharField, DateField, TextField
from django.db.models.fields.files import ImageField
from django.core.validators import MaxValueValidator
from django import forms

class Publicacion(models.Model):
    CONSOLE_CHOICES = [
        ('Xbox', 'Xbox'),
        ('PC', 'PC'),
        ('Nintendo Switch', 'Nintendo Switch'),
        ('PS5', 'PS5'),
        ('Sin Información', 'Sin Información')
    ]
    CATEGORY = [
        ('Acción', "Acción"),
        ('Aventura', 'Aventura'),
        ('Familiar','Familiar'),
        ('Deporte','Deporte'),
        ('Terror', 'Terror')
    ]
    title = CharField(max_length=100)
    opinion = TextField(max_length=1000)
    console = CharField(max_length=20, choices=CONSOLE_CHOICES)
    release_date = DateField()
    category = CharField(max_length=20,choices=CATEGORY)
    front_page = ImageField(upload_to='BeyondGames/images/',blank=False, default='media/BeyondGames/images/no_disponible.png')
    create_date = DateField(auto_now_add=True)

    def __str__(self):
        return self.title
# Generated by Django 5.0 on 2023-12-16 02:56

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BeyondGames', '0002_publicacion_front_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='create_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
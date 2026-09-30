from django.contrib import admin
from .models import Categoria, Producto

# Registra el modelo Categoria para que sea visible y gestionable en el panel de administración.
admin.site.register(Categoria)

# Registra el modelo Producto para que sea visible y gestionable en el panel de administración.
admin.site.register(Producto)


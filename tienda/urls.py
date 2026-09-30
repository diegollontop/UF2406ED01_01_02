from django.contrib import admin
from django.urls import path, include
from productos import views as productos_views

urlpatterns = [
    # Ruta para acceder al panel de administración de Django
    path("admin/", admin.site.urls),

    # Incluye las rutas de la aplicación de productos
    path("", include("productos.urls")),

    # Incluye las rutas del sistema de autenticación nativo de Django (login, logout, etc.)
    path("accounts/", include("django.contrib.auth.urls")),
]


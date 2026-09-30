from django.urls import path
from . import views

urlpatterns = [
    # --- Páginas Base ---
    # Ruta raíz que carga la página de inicio del sitio web
    path("", views.home, name="home"),
    # Ruta para el formulario de registro de nuevos usuarios
    path("register/", views.register, name="register"),

    # --- CRUD de Categorías ---
    # Muestra el listado completo de categorías existentes
    path("categorias/", views.categoria_lista, name="categoria_lista"),
    # Formulario para dar de alta una nueva categoría
    path("categorias/nueva/", views.categoria_crear, name="categoria_crear"),
    # Permite modificar una categoría específica identificada por su ID único (pk)
    path("categorias/<int:pk>/editar/", views.categoria_editar, name="categoria_editar"),
    # Permite borrar una categoría específica identificada por su ID único (pk)
    path("categorias/<int:pk>/eliminar/", views.categoria_eliminar, name="categoria_eliminar"),

    # --- CRUD de Productos ---
    # Muestra el catálogo con todos los productos disponibles
    path("productos/", views.producto_lista, name="producto_lista"),
    # Despliega la información detallada de un producto mediante su ID único (pk)
    path("productos/<int:pk>/", views.producto_detalle, name="producto_detalle"),
    # Formulario para publicar un nuevo producto en el catálogo
    path("productos/nuevo/", views.producto_crear, name="producto_crear"),
    # Permite modificar un producto específico identificado por su ID único (pk)
    path("productos/<int:pk>/editar/", views.producto_editar, name="producto_editar"),
    # Permite borrar un producto específico identificado por su ID único (pk)
    path("productos/<int:pk>/eliminar/", views.producto_eliminar, name="producto_eliminar"),
]

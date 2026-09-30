# Decorador para restringir el acceso a vistas solo a usuarios autenticados
from django.contrib.auth.decorators import login_required
# Función para iniciar la sesión de un usuario en el sistema
from django.contrib.auth import login
from django.shortcuts import (
    render,             # Renderiza plantillas HTML con datos de contexto
    redirect,           # Redirecciona al usuario a otra URL o vista
    get_object_or_404,  # Busca un objeto en la base de datos o devuelve un error 404 si no existe
)
# Modelos de la base de datos para interactuar con las tablas de categorías y productos
from .models import Categoria, Producto
# Formularios personalizados para la captura y validación de datos en la aplicación
from .forms import (
    RegistroForm,
    CategoriaForm,
    ProductoForm,
)

def home(request):
    # Renderiza la página principal del sitio utilizando la plantilla home.html.
    return render(request, "home.html")


def register(request):
    # Maneja el registro de nuevos usuarios, inicia sesión automáticamente y redirecciona.
    if request.user.is_authenticated:
        return redirect("home")
        
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect("home")
    else:
        form = RegistroForm()
        
    return render(
        request,
        "registration/register.html",
        {
            "form": form
        }
    )

@login_required
def categoria_lista(request):
    # Obtiene todas las categorías de la base de datos y las muestra en una lista.
    categorias = Categoria.objects.all()
    return render(
        request,
        "categorias/lista.html",
        {
            "categorias": categorias
        }
    )


@login_required
def categoria_crear(request):
    # Maneja la creación de una nueva categoría mediante un formulario POST.
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("categoria_lista")
    else:
        form = CategoriaForm()
        
    return render(
        request,
        "categorias/formulario.html",
        {
            "form": form,
            "titulo": "Nueva categoría",
        }
    )


@login_required
def categoria_editar(request, pk):
    # Busca una categoría por su clave primaria (pk) y permite editar sus datos."""
    categoria = get_object_or_404(
        Categoria,
        pk=pk
    )
    if request.method == "POST":
        form = CategoriaForm(
            request.POST,
            instance=categoria
        )
        if form.is_valid():
            form.save()
            return redirect("categoria_lista")
    else:
        form = CategoriaForm(
            instance=categoria
        )
        
    return render(
        request,
        "categorias/formulario.html",
        {
            "form": form,
            "titulo": "Editar categoría",
        }
    )


@login_required
def categoria_eliminar(request, pk):
    # Busca una categoría por su clave primaria (pk) y la elimina si se confirma la petición POST.
    categoria = get_object_or_404(
        Categoria,
        pk=pk
    )
    if request.method == "POST":
        categoria.delete()
        return redirect("categoria_lista")
        
    return render(
        request,
        "categorias/eliminar.html",
        {
            "categoria": categoria
        }
    )


def producto_lista(request):
    # Obtiene todos los productos con su respectiva categoría y los muestra en una lista. 
    productos = Producto.objects.select_related(
        "categoria"
    )
    return render(
        request,
        "productos/lista.html",
        {
            "productos": productos
        }
    )


def producto_detalle(request, pk):
    # Busca un producto específico por su ID (pk) y muestra su información detallada.
    producto = get_object_or_404(
        Producto,
        pk=pk
    )
    return render(
        request,
        "productos/detalle.html",
        {
            "producto": producto
        }
    )


@login_required
def producto_crear(request):
    # Maneja la creación de un nuevo producto mediante un formulario POST.
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("producto_lista")
    else:
        form = ProductoForm()
        
    return render(
        request,
        "productos/formulario.html",
        {
            "form": form,
            "titulo": "Nuevo producto",
        }
    )


@login_required
def producto_editar(request, pk):
    # Busca un producto por su clave primaria (pk) y permite editar sus datos.
    producto = get_object_or_404(
        Producto,
        pk=pk
    )
    if request.method == "POST":
        form = ProductoForm(
            request.POST,
            instance=producto
        )
        if form.is_valid():
            form.save()
            return redirect("producto_lista")
    else:
        form = ProductoForm(
            instance=producto
        )
        
    return render(
        request,
        "productos/formulario.html",
        {
            "form": form,
            "titulo": "Editar producto",
        }
    )


@login_required
def producto_eliminar(request, pk):
    # Busca un producto por su clave primaria (pk) y lo elimina si se confirma la petición POST.
    producto = get_object_or_404(
        Producto,
        pk=pk
    )
    if request.method == "POST":
        producto.delete()
        return redirect("producto_lista")
        
    return render(
        request,
        "productos/eliminar.html",
        {
            "producto": producto
        }
    )





from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Categoria, Producto

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]
    
    def clean_email(self):
        # Función que valida que el correo electrónico no esté registrado por otro usuario.
        email = self.cleaned_data.get("email")

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "Ya existe un usuario con este correo electrónico."
            )
    
        return email


class CategoriaForm(forms.ModelForm):
    # Clase interna de configuración (Meta) para el formulario de Categorías.
    class Meta:
        model = Categoria
        fields = [
            "nombre",
            "descripcion",
        ]

class ProductoForm(forms.ModelForm):
    # Clase interna de configuración (Meta) para el formulario de Productos.
    class Meta:
        model = Producto
        fields = [
            "nombre",
            "descripcion",
            "precio",
            "categoria",
        ]

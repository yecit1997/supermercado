from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'categoria', 'stock', 'imagen']

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio is None or precio < 0:
            raise forms.ValidationError("El precio debe ser un número positivo.")
        return precio

    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock is None or stock < 0:
            raise forms.ValidationError("El stock debe ser 0 o un número positivo.")
        return stock

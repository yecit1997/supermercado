# productos/views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Producto
from .forms import ProductoForm

# Lista de productos: paginación y búsqueda simple pueden añadirse aquí
class ProductoListView(ListView):
    model = Producto
    template_name = 'productos/lista.html'     # plantilla a renderizar
    context_object_name = 'productos'          # nombre de la variable en template
    paginate_by = 20                           # opcional: paginar 20 por página

    # Si quieres filtrar por búsqueda GET, puedes sobrescribir get_queryset:
    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     q = self.request.GET.get('q')
    #     if q:
    #         qs = qs.filter(nombre__icontains=q)
    #     return qs


# Detalle de un producto
class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'productos/detalle.html'
    context_object_name = 'producto'


# Crear producto
class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'productos/form.html'
    success_url = reverse_lazy('productos:lista')  # nombre de la url después de crear

    # puedes añadir lógica extra al guardar en form_valid:
    # def form_valid(self, form):
    #     # por ejemplo, setear campos automáticos
    #     return super().form_valid(form)


# Actualizar producto
class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'productos/form.html'
    success_url = reverse_lazy('productos:lista')


# Eliminar producto
class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'productos/confirmar_eliminar.html'
    success_url = reverse_lazy('productos:lista')

from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path('', views.ProductoListView.as_view(), name='lista'),
    path('crear/', views.ProductoCreateView.as_view(), name='crear'),
    path('detalle/<str:uuid>/', views.ProductoDetailView.as_view(), name='detalle'),
    path('editar/<str:uuid>/', views.ProductoUpdateView.as_view(), name='editar'),
    path('eliminar/<str:uuid>/', views.ProductoDeleteView.as_view(), name='eliminar'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.supplier_index, name='supplier_index'),
    path('createsupplier/', views.supplier_create, name='supplier_create'),
    path('editsupplier/<int:supplierid>/', views.supplier_edit, name='supplier_edit'),
]

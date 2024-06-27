from django.urls import path
from . import views

urlpatterns = [
    path('', views.store_index, name='store_index'),
    path('createstores/', views.store_create, name='store_create'),
    path('editstores/<int:storeid>/', views.store_edit, name='store_edit'),
]

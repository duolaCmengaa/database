from django.urls import path
from . import views


urlpatterns = [
    path("", views.index,name = "orders"),
    path("editorders/<int:orderid>", views.edit),
    path('summary/', views.summary, name='order_summary'),
]

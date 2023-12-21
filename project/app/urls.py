from django.urls import path
from .views import menu, order, create, delete

urlpatterns = [
    path('menu/', menu, name='menu'),
    path('order/', order, name='order'),
    path('create/', create, name='create'),
    path('delete/<int:id>', delete, name='delete'),
]

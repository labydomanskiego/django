from django.urls import path
from .views import view_jedzenie, add_jedzenie, delete_jedzenie, get_jedzenie, modify_jedzenie
urlpatterns = [
    path('', view_jedzenie, name='view_jedzenie'),
    path('add/', add_jedzenie, name='add_jedzenie'),
    path('modify/', modify_jedzenie, name='modify_jedzenie'),
    path('delete/<int:id>/', delete_jedzenie, name='delete_jedzenie'),
    path('get/<int:id>/', get_jedzenie, name='get_jedzenie'),
]

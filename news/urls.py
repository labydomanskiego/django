from django.urls import path
from .views import view_news, add, get, modify
urlpatterns = [
    path('news/', view_news, name='view_news'),
    path('news/add/', add, name="add"),
    path('news/<int:id>/', get, name='get'),
    path('news/modify/', modify, name='modify')
]

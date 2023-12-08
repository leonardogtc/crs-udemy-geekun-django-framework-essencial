# Faz a importação do path da biblioteca urls
from django.urls import path

# Faz a importação da views
from .views import index, contato, produto


urlpatterns = [
    path('', index, name='index'),
    path('contato', contato, name='contato'),
    path('produto/<int:pk>', produto, name='produto')
]

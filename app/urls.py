'''
Criando uma página de Views aqui para otimizar o processo ao invés de ficar criando esse processo no urls do core.

primeiramente eu fiz o import do path pra poder usar caminhos, e importei a views do meu app para vizualizar a aplicação.
'''

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = 'index'),
    path('save/', views.save, name='save'),
    path('edit/<int:sample_id>/', views.edit, name='edit'),
    path('delete/<int:sample_id>/', views.delete, name='delete'),

]

'''
Lembrar de usar usar [] para as aplicações.
'''
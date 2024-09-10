from django.urls import path
from . import views

urlpatterns = [
    path('inserir/', views.inserir_nota, name='inserir_nota'),
    path('notas/', views.listar_notas, name='listar_notas'),
    path('media/<str:aluno>/', views.media_aluno, name='media_aluno'),
]
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.lista_tarefas, name='lista_tarefas'),
    path('excluir/<int:tarefa_id>/', views.excluir_tarefa, name='excluir_tarefa'),
    path('editar/<int:tarefa_id>/', views.editar_tarefa, name='editar_tarefa'),
    path('marcar_concluida/<int:tarefa_id>/', views.marcar_concluida, name='marcar_concluida'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('cadastro/', views.cadastrar_usuario, name='cadastrar_usuario'),
]

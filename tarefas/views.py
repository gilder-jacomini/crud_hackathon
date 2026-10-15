from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa

# Create your views here.
def lista_tarefas(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        
        if titulo:
            Tarefa.objects.create(titulo=titulo)

        return redirect('lista_tarefas')

    tarefas = Tarefa.objects.all()
    return render(request, 'tarefas/lista.html', {'tarefas': tarefas})

def excluir_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)

    if request.method == 'POST':
        tarefa.delete()

    return redirect('lista_tarefas')

def editar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)

    if request.method == 'POST':
        tarefa.titulo = request.POST.get('titulo')
        tarefa.save()
        return redirect('lista_tarefas')

    return render(request, 'tarefas/editar.html', {'tarefa': tarefa})

def marcar_concluida(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)

    if request.method == 'POST':
        tarefa.concluida = not tarefa.concluida
        tarefa.save()

    return redirect('lista_tarefas')
from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages



# Create your views here.
@login_required
def lista_tarefas(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo').strip()
        
        if titulo:
            Tarefa.objects.create(titulo=titulo, usuario=request.user)

        return redirect('lista_tarefas')

    tarefas = Tarefa.objects.filter(usuario=request.user)
    return render(request, 'tarefas/lista.html', {'tarefas': tarefas})

@login_required
def excluir_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)

    if request.method == 'POST':
        tarefa.delete()

    return redirect('lista_tarefas')

@login_required
def editar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id, usuario=request.user)

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

def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('lista_tarefas')
    else:
            form = UserCreationForm()

    return render(request, 'registration/cadastro.html', {'form': form})
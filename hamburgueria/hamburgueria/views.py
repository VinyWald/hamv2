from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login  # Importe a função de login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Pedido
from .forms import BurgerForm


def home(request):
    return render(request, 'index.html')

@login_required
def fazer_pedido(request):
    if request.method == 'POST':
        form = BurgerForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.cliente = request.user
            pedido.save()
            form.save_m2m()  # Salvar as relações ManyToMany após salvar o objeto principal
            messages.success(request, 'Pedido realizado com sucesso!')
            return redirect('pagina_de_sucesso')
        else:
            messages.error(request, 'Erro ao realizar o pedido. Por favor, verifique os dados inseridos.')
    else:
        form = BurgerForm()
    
    # Obtém os últimos 5 pedidos feitos pelo cliente
    pedidos_recentes = Pedido.objects.filter(cliente=request.user).order_by('-dataPedido')[:5]
    
    return render(request, 'montarPedido.html', {'form': form, 'pedidos_recentes': pedidos_recentes})
def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Login bem-sucedido!')
            return redirect('home')
        else:
            messages.error(request, 'Falha no login. Verifique suas credenciais.')
    
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    messages.success(request, 'Você foi desconectado com sucesso.')
    return redirect('home')

def registro(request):
    if request.method == 'POST':
        print("Requisição de método POST recebida.")  # Mensagem de depuração
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print("Formulário é válido.")  # Mensagem de depuração
            user = form.save()
            auth_login(request, user)
            messages.success(request, 'Registro bem-sucedido! Você foi autenticado automaticamente.')
            return redirect('home')
        else:
            print("Formulário inválido.")  # Mensagem de depuração
            messages.error(request, 'Erro no registro. Por favor, verifique os dados inseridos.')
    else:
        print("Requisição de método GET recebida.")  # Mensagem de depuração
        form = UserCreationForm()

    return render(request, 'registro.html', {'form': form})

@login_required
def pagina_de_sucesso(request):
    pedidos = Pedido.objects.filter(cliente=request.user).order_by('-dataPedido')
    if pedidos:
        mensagem = 'Seus pedidos foram realizados com sucesso!'
    else:
        mensagem = 'Você ainda não fez nenhum pedido.'
    
    return render(request, 'pagina_de_sucesso.html', {'mensagem': mensagem})

@login_required
def meus_pedidos(request):
    pedidos = Pedido.objects.filter(cliente=request.user).order_by('-dataPedido')
    return render(request, 'meus_pedidos.html', {'pedidos': pedidos})
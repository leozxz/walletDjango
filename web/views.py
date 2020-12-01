from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import Transacao
from .forms import TransacaoForm



# Create your views here.

def homepage(request):
    return render(request, 'index.html')

@login_required(login_url='/login/')
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required(login_url='/login/')
def profile(request):
    if request.method == "POST":
        form_senha = PasswordChangeForm(request.user, request.POST)
        if form_senha.is_valid():
            user = form_senha.save()
            update_session_auth_hash(request, user)
            return redirect('index')
    else:
        form_senha = PasswordChangeForm(request.user)
    return render(request, 'profile.html', {'form_senha': form_senha})

def login_user(request):
    return render(request, 'login.html')

@csrf_protect
def submit_login(request):
    if request.POST:
      username = request.POST.get('username')
      password = request.POST.get('password')
      print(username)
      print(password)
      user = authenticate(username = username, password = password)
      if user is not None:
          login(request, user)
          return redirect('/dashboard')
      else:
          messages.error(request, 'Usuario e senha invalida! Favor, tentar novamente.')
          return redirect('/login/')

def logout_user(request):
    logout(request)
    return redirect('/login/')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required(login_url='/login/')
def comprar(request):
    if request.method == 'POST':

        form = TransacaoForm(request.POST)
        if form.is_valid():
            real = form['real'].value()
            cripto = form['cripto'].value()
            transacao = Transacao(real=real, cripto=cripto)
            transacao.save()
            return redirect('carteira')
        else:
            messages.error(request, 'Algo deu errado!')
            return redirect('/dashboard/comprar')
    else:
        transacoes = Transacao.objects.all()

    return render(request, 'comprar.html', {'transacoes':transacoes})

@login_required(login_url='/login/')
def vender(request):
    return render(request, 'vender.html')
@login_required(login_url='/login/')
def carteira(request):
    valor = Transacao.objects.get(id=1)
    return render(request, 'carteira.html', {'valor':valor})

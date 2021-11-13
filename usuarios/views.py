from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth



def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']

        if not nome.strip():
            # Adicionar mensagem de erro ao usuario
            return redirect('cadastro')
        if not email.strip():
            # Adicionar mensagem de erro ao usuario
            return redirect('cadastro')
        if senha != senha2:
            # Adicionar mensagem de senhas diferentes
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            # Adicionar mensagem de usuario ja cadastrado
            return redirect('cadastro')
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        print('usuario cadastrado com sucesso')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if email == '' or senha == '':
            #Mensagem de campos vazios
            return redirect('login')
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                print('lOGIN REALIZADO COM SUCESSO')
                return redirect('dashboard')
        return redirect('dashboard')
    return render(request, 'usuarios/login.html')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'usuarios/dashboard.html')
    else:
        return redirect('index')

def logout(request):
    auth.logout(request)
    return redirect('index')

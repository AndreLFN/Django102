from django.shortcuts import redirect, render
from django.contrib.auth.models import User



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
    return render(request, 'usuarios/login.html')

def dashboard(request):
    pass

def logout(request):
    pass

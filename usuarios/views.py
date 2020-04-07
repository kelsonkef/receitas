from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from receitas.models import Receita

# Create your views here.

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        email = request.POST['email']
        if not nome.strip():
            print('O Nome não pode ficar em branco')
            return redirect('cadastro')
        print(nome, senha, email,senha2)
        if not email.strip():
            print('O campo email não pode ficar em branco')
            return redirect('cadastro')
        if senha != senha2:
            print('As senhas não são iguais')
            return redirect('cadastro')
        if User.objects.filter(email = email).exists():# Verificar se existe o email já cadastrado no banco de dados
            print('Usuario já Cadastrado')
            return redirect('cadastro')
        user = User.objects.create_user(username=nome, email = email, password=senha)#Cria um objeto Usuario
        user.save()
        print('Usuario cadastrato com Sucesso')
        return redirect('login')
    return render(request, 'usuarios/cadastro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if email == "" or senha == "":
            print('Os campos email e senha não podem ficar em branco')
            return redirect('login')
        print(email, senha)
        if User.objects.filter(email=email).exists(): # verifico se existe o emial no banco de dados
            nome = User.objects.filter(email=email).values_list('username', flat=True).get() # pego o usuraio que tem o email informado
            user = auth.authenticate(request, username=nome, password=senha) # faço a autenticação com o retorno do nome do usurai do banco de dados.
            if user is not None: # verifco se o usuario não está nulo
                auth.login(request, user) # realizo o login
                print('Login realizado com sucesso')
                return redirect('dashboard')
    return render(request, 'usuarios/login.html')


def dashboard(request):
    if request.user.is_authenticated: # verifico o usuario está autenticado
        id = request.user.id
        print("O Id do meu usuario é :"+str(id))
        receitas = Receita.objects.order_by('-data_receita').filter(pessoa=id)
        for receita in receitas:
            print(receita.nome_receita)
        dados = {
            'receitas' : receitas
        }
        print("entrnado no segundo for")
        for receita in dados['receitas']:
            print(receita.nome_receita)
        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')

def logout(request):
    auth.logout(request)
    return redirect('index')

def criar_receita(request):
    if request.method == 'POST':
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto_receita = request.FILES['foto_receita']
        user = get_object_or_404(User, pk=request.user.id)
        receita = Receita.objects.create(pessoa = user,nome_receita = nome_receita , ingredientes = ingredientes, modo_preparo =modo_preparo,
         tempo_preparo = tempo_preparo, rendimento = rendimento, categoria = categoria, foto_receita = foto_receita)
        receita.save()
        return redirect('dashboard')
        
    else:
        return render(request, 'usuarios/criar_receita.html')



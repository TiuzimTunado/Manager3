from django.shortcuts import render, redirect
from .models import Disciplina, Nota, Usuario
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout

def inserir_nota(request):
    if not request.user.id:
        return redirect('/')
    if request.method == "POST":
        aluno = request.user.username
        disciplina_id = request.POST.get('disciplina')
        nota = request.POST.get('nota')
        disciplina = Disciplina.objects.get(id=disciplina_id)
        Nota.objects.create(aluno=aluno, disciplina=disciplina, nota=nota)
        return redirect('listar_notas')
    disciplinas = Disciplina.objects.all()
    return render(request, 'HTML/inserirnota.html', {'disciplinas': disciplinas})

def listar_notas(request):
    if not request.user.id:
        return redirect('/')
    notas = Nota.objects.filter(aluno=request.user.username)
    return render(request, 'HTML/listanotas.html', {'notas': notas})

def media_aluno(request, aluno):
    notas = Nota.objects.filter(aluno=aluno)
    if notas:
        media = sum(nota.nota for nota in notas) / notas.count()
    else:
        media = 0
    return render(request, 'HTML/mediaaluno.html', {'aluno': aluno, 'media': media})

def login(request):
    if request.user.id:
        return redirect('/inserir')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return redirect('/inserir')
    return render(request, 'HTML/login.html')

def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.nome = request.Post.get('nome')
    novo_usuario.idade = request.Post.get('idade')
    novo_usuario.save()

    usuarios = {
        'usuarios': Usuario.objects.all
    }
    
    return render(request, 'usuarios/usuarios.html', usuarios=usuarios)

def cadastro_usuario(request):
    if request.method == "POST":
        try:
            usuario_email = User.objects.get(email=request.POST.get('email'))
            usuario_username = User.objects.get(email=request.POST.get('username'))

            if usuario_email or usuario_username:
                return render(request, 'HTML/cadastro.html', {'erro': 'Erro! Já existe um usuário com o mesmo e-mail ou mesmo username'})
        except User.DoesNotExist:
                username = request.POST.get('username')
                email = request.POST.get('email')
                password = request.POST.get('password')
                password_confirmation = request.POST.get('password_confirmation')
                if password == password_confirmation:
                    new_user = User.objects.create_user(username=username, password=password, email=email, is_superuser=1, is_staff=1)
                    new_user.save()
                    return redirect('/')
    else:
        return render(request, 'HTML/cadastro.html')

def sair(request):
    logout(request)
    return redirect("/")





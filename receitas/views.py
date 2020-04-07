from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from .models import Receita
# Create your views here.

def index(request):
    #Filtarando e ordenando
    receitas = Receita.objects.order_by('-data_receita').filter(publicada=True) # Select * from Receitas where publicada = True order by data_receita desc
    dados = {
        'receitas' : receitas,
        'novo': 'Teste da View'
    }
    return render(request,"index.html",dados)

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id) #Pega o Objeto ou dá erro 404

    receita_a_exibir = {
        'receita': receita
    }
    return render(request,"receita.html", receita_a_exibir)

def buscar(request):
    lista_receitas = None
    if 'buscar' in request.GET:# se tem o paramentro buscar dentro do GET
        lista_receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)
        nome_da_busca= request.GET['buscar']
        if buscar: #Se buscar tiver preenchido
            lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_da_busca) # o __icontains funciona como um like do SQL
    dados = {
        'receitas': lista_receitas
    }

    return render(request, 'buscar.html', dados)
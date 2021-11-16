from django.shortcuts import get_object_or_404, render, redirect
from receitas.models import Receita



def buscar(request):
    lista_receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar'] # o 'search' é referente ao atributo nome=search da tag <input> do formulário de busca na página de index
        lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar)
    
    dados = {
        'receitas': lista_receitas
    }

    return render(request, 'receitas/buscar.html', dados)
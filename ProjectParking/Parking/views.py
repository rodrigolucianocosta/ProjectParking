#encoding:utf-8
from django.shortcuts import render

def index(request):
    context = {'texto': 'Projeto Django no Linux/Ubuntu com Sublime Text 3 avaliação 2'}
        
    return render(request, 'Parking/index.html', context)

def servicos(request):
	context = {'texto': 'pagina de servicos'}
	return render(request, 'Parking/servicos.html',context)

def localizacao(request):
	context = {'texto': 'pagina de localizaco'}
	return render(request, 'Parking/localizacao.html',context)

def quemsomos(request):
	context = {'texto': 'pagina sobre quem somos'}
	return render(request,'Parking/quemsomos.html',context)

def faleconosco(request):
	context = {'texto': 'pagina fale conosco'}
	return render(request,'Parking/faleconosco.html',context)



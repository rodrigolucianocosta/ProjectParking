#encoding:utf-8
from django.shortcuts import render, redirect
from forms import ClienteForm
from models import cliente

def index(request):
    context = {'texto': 'Projeto Django no Linux/Ubuntu com Sublime Text 3 avaliação 2'}
        
    return render(request, 'Parking/index.html', context)

def CadastraCliente(request):
	if request.method == 'POST':
		form = ClienteForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('clientes')
	else:
		form = ClienteForm()
	return render(request,"Parking/cadastracliente.html",{'form':form})

def CadastraVeiculo(request):
	context = {'texto': 'pagina de localizaco'}
	return render(request, 'Parking/cadastraveiculo.html',context)

def CadastraVaga(request):
	context = {'texto': 'pagina sobre quem somos'}
	return render(request,'Parking/cadastravaga.html',context)




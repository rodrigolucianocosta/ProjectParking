#encoding: utf-8
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from forms import ClienteForm,VeiculoForm,VagaForm
from models import cliente

def index(request):
    context = {'texto': 'Projeto Django no Linux/Ubuntu com Sublime Text 3 avaliação 2'}
        
    return render(request, 'Parking/index.html', context)

def ListaCliente(request,codigo=None):
	if codigo:
		rone = cliente.objects.filter(pk=codigo)
	else:
		rone = cliente.objects.all()

	if request.method == "POST":
		query = request.POST.get('query')
		rtwo =	cliente.objects.filter(nome_contains=query)
	else:
		rtwo = cliente.objects.all()

	context = { 
	'ListaCliente': rone,
	}
	return render(request,"Parking/listacliente.html",context)


def CadastraCliente(request):
	if request.method == 'POST':
		form = ClienteForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('cadastraVeiculo')
	else:
		form = ClienteForm()
	return render(request,"Parking/cadastracliente.html",{'form':form})


def AlteraCliente(request,codigo=None):
	objeto = get_object_or_404(cliente,pk=codigo)

	if request.method =='POST':
		form = ClienteForm(request.POST,instance=objeto)

		if form.is_valid():
			form.save()
			return redirect('listacliente')
		else:
			form = ClienteForm(instance=objeto)
			return render(request,"Parking/alteracliente.html",{'form':form})


#==========================================================================================

def CadastraVeiculo(request):
	if request.method =='POST':
		form = VeiculoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('cadastravaga')
	else:
		form = VeiculoForm()
	return render(request,'Parking/cadastraveiculo.html',{'form':form})
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def CadastraVaga(request):
	if request.method == 'POST':
		form = VagaForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		form = VagaForm()
	return render(request,'Parking/cadastravaga.html',{'form':form})

 


#encoding:utf-8
from django.shortcuts import render, redirect,get_object_or_404
from forms import ClienteForm,VeiculoForm,VagaForm
from models import cliente

def index(request):
    context = {'texto': 'Projeto Django no Linux/Ubuntu com Sublime Text 3 avaliação 2'}
        
    return render(request, 'Parking/index.html', context)


def CadastraCliente(request):
	if request.method == 'POST':
		form = ClienteForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('cadastraVeiculo')
	else:
		form = ClienteForm()
	return render(request,"Parking/cadastracliente.html",{'form':form})

#==========================================================================================

def CadastraVeiculo(request):
	if request.method =='POST':
		formVeiculo = VeiculoForm(request.POST)
		if formVeiculo.is_valid():
			formVeiculo.save()
			return redirect('cadastravaga')
	else:
		form = VeiculoForm()
	return render(request,'Parking/cadastraveiculo.html',{'formVeiculo':form})
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def CadastraVaga(request):
	if request.method == 'POST':
		formVaga = VagaForm(request.POST)
		if formVaga.is_valid():
			formVaga.save()
			return redirect('cadastraVaga')
	else:
		form = VagaForm()
	return render(request,'Parking/cadastravaga.html',{'formVaga':form})

 


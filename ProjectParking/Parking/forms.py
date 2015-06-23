#encoding: utf-8 
from django import forms
from models import cliente,veiculo,vaga

class ClienteForm(forms.ModelForm):
	class Meta:
		model = cliente
		fields = ['nome','email','cpf','rg','telefone']

class VeiculoForm(forms.ModelForm):
	class Meta:
		model = veiculo
		fields = ['cliente','tipoVeiculo','fabricante','marca','cor','placa']

class VagaForm(forms.ModelForm):
	class Meta:
		model = vaga
		fields = ['cliente','numero','bloco','entrada','saida','valorHora']


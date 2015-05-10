#coding:utf-8 
from django import forms
from models import cliente

class ClienteForm(forms.ModelForm):
	class Meta:
		model = cliente
		fields = ['nome','email','cpf','rg','telefone']



#encoding: utf-8
from django.contrib import admin
from models import vaga,veiculo,cliente
# Register your models here.

class vagaAdmin(admin.ModelAdmin):
	list_display = ['numero','bloco','entrada','saida','valorHora']
	save_as=True

class veiculoAdmin(admin.ModelAdmin):
	list_display = ['fabricante','marca','placa','cor']
	save_as=True

class clienteAdmin(admin.ModelAdmin):
	list_display = ['nome','email','cpf','rg','telefone']
	save_as=True

	

admin.site.register(vaga,vagaAdmin)
admin.site.register(veiculo,veiculoAdmin)
admin.site.register(cliente,clienteAdmin)

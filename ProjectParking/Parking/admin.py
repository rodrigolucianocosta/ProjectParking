from django.contrib import admin
from models import vaga,carro,cliente
# Register your models here.

class vagaAdmin(admin.ModelAdmin):
	list_display = ['numero','bloco','Entrada','Saida','ValorHora']
	save_as=True

class carroAdmin(admin.ModelAdmin):
	list_display = ['fabricante','marca','placa','cor']
	save_as=True

class clienteAdmin(admin.ModelAdmin):
	list_display = ['nome','cpf','rg','telefone']
	save_as=True

	

admin.site.register(vaga,vagaAdmin)
admin.site.register(carro,carroAdmin)
admin.site.register(cliente,clienteAdmin)

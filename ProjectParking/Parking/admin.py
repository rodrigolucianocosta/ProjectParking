from django.contrib import admin
from models import vaga,carro,cliente
# Register your models here.

class vagaAdmin(admin.ModelAdmin):
	list_display = ['numero','bloco']

class carroAdmin(admin.ModelAdmin):
	list_display = ['fabricante','marca','placa','cor']

class clienteAdmin(admin.ModelAdmin):
	list_display = ['nome','cpf','rg','telefone']


admin.site.register(vaga,vagaAdmin)
admin.site.register(carro,carroAdmin)
admin.site.register(cliente,clienteAdmin)

from django.contrib import admin
from models import vaga,carro
# Register your models here.

class vagaAdmin(admin.ModelAdmin):
	list_display = ['numero','bloco']


class carroAdmin(admin.ModelAdmin):
	list_display = ['fabricante']

admin.site.register(vaga,vagaAdmin)
admin.site.register(carro,carroAdmin)

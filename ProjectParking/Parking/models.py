#unicode: utf-8
from django.db import models

# Create your models here.
class vaga(models.Model):
	numero = models.IntegerField('numero da vaga',max_length=2)
	bloco  = models.CharField('bloco',max_length=2)
	horarioEntrada = models.DateTimeField(auto_now=True,null=True)
	horarioSaida = models.DateTimeField(auto_now=True,null=True)

	def __unicode__(self):
		return u"%d %s"(self.numero,self.bloco)

class carro(models.Model):
	fabricante = models.CharField('fabricante',max_length=20)
	marca = models.CharField('marca',max_length=20,null=True)
	cor = models.CharField('cor',max_length=10,null=True)
	placa = models.CharField('placa do veiculo',max_length=10,null=True)
	def __unicode__(self):
		return u"%s %s %s %s"%(self.fabricante,self.marca,self.cor,self.placa)

class cliente(models.Model):
	carro = models.ForeignKey(carro)
	nome = models.CharField('nome',max_length=50)
	cpf = models.IntegerField('cpf',max_length=11)
	rg = models.CharField('rg',max_length=20)
	#endereco = 
	telefone = models.IntegerField('telefone',max_length=9)
	def __unicode__(self):
		return u"%s %d %s %d"%(self.nome,self.cpf,self.rg,self.telefone)

#encoding: utf-8
from django.db import models
from django import forms
from django.core.validators import MinValueValidator,MaxValueValidator
TIPO_VAGA=[
		('A','Carro'),
		('B','Moto'),
		('C','Caminhao'),
		]

TIPO_VEICULO=[
		('A','carro'),
		('B','moto'),
		('C','Caminhao')

]

class cliente(models.Model):
	nome = models.CharField('nome',max_length=50)
	email = models.EmailField('email',max_length=50,null=True)
	cpf = models.IntegerField('cpf')
	rg = models.CharField('rg',max_length=20)
	telefone = models.IntegerField('telefone')
	
	
	class Meta:
		verbose_name = "cliente"
		verbose_name_plural = "clientes"


	def __unicode__(self):
		return u"%s %d %s %d"%(self.nome,self.cpf,self.rg,self.telefone)


class veiculo(models.Model):
	cliente = models.ForeignKey(cliente, verbose_name="cliente",null=True)
	tipoVeiculo = models.CharField('Tipo de veiculo',max_length=1,choices=TIPO_VEICULO,null=True)
	fabricante = models.CharField('fabricante',max_length=20,null=True)
	marca = models.CharField('marca',max_length=20,null=True)
	cor = models.CharField('cor',max_length=10,null=True)
	placa = models.CharField('placa do veiculo',max_length=10,null=True)


	class Meta:
		verbose_name = "veiculo"
		verbose_name_plural = "veiculos"
	

	def __unicode__(self):
		return u"%s %s %s %s"%(self.fabricante,self.marca,self.cor,self.placa)

class vaga(models.Model):
	
	#tipoVaga = models.CharField('Tipo de Vaga',max_length=1,choices=TIPO_VAGA,null=True)
	cliente = models.OneToOneField(cliente,verbose_name="cliente",null=True)	
	numero = models.AutoField('numero da vaga',primary_key=True)
	bloco  = models.CharField('bloco',max_length=2)
	entrada = models.DateTimeField('entrada',null=True)
	saida = models.DateTimeField('Saida',null=True)
	valorHora = models.FloatField('valorHora',validators=[MinValueValidator(2.00),MaxValueValidator(10)],null=True)

	class Meta:
		verbose_name = "vaga"
		verbose_name_plural = "vagas"

	def __unicode__(self):
		return u"%d %s %s %s %f"%(self.numero,self.bloco,self.entrada,self.saida,self.valorHora)
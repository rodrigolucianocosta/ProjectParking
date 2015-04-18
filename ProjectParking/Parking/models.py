#unicode: utf-8
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
TIPO_VAGA=[
		('A','Carro'),
		('B','Moto'),
		('C','Caminhao')
		]

class carro(models.Model):
	fabricante = models.CharField('fabricante',max_length=20)
	marca = models.CharField('marca',max_length=20,null=True)
	cor = models.CharField('cor',max_length=10,null=True)
	placa = models.CharField('placa do veiculo',max_length=10,null=True)

	class Meta:
		verbose_name = "carro"
		verbose_name_plural = "carros"
	
	def __unicode__(self):
		return u"%s %s %s %s"%(self.fabricante,self.marca,self.cor,self.placa)



class cliente(models.Model):
	carro = models.ForeignKey(carro, verbose_name="carro")
	nome = models.CharField('nome',max_length=50)
	cpf = models.IntegerField('cpf',max_length=11)
	rg = models.CharField('rg',max_length=20)
	#endereco = 
	telefone = models.IntegerField('telefone',max_length=9)
	
	class Meta:
		verbose_name = "cliente"
		verbose_name_plural = "clientes"

	def __unicode__(self):
		return u"%s %d %s %d"%(self.nome,self.cpf,self.rg,self.telefone)

class vaga(models.Model):
	
	tipoVaga = models.CharField('Tipo de Vaga',max_length=1,choices=TIPO_VAGA)
	cliente = models.OneToOneField(cliente,verbose_name="cliente",null=True)
	#carro = models.OneToOneField(carro,verbose_name="carro",null=True)
	numero = models.AutoField('numero da vaga',primary_key=True)
	bloco  = models.CharField('bloco',max_length=2)
	Entrada = models.DateTimeField('Entrada',null=True)
	Saida = models.DateTimeField('Saida',null=True)
	ValorHora = models.FloatField('valorHora',validators=[MinValueValidator(2.00),MaxValueValidator(10)],null=True)

	class Meta:
		verbose_name = "vaga"
		verbose_name_plural = "vagas"

	def __unicode__(self):
		return u"%d %s"(self.numero,self.bloco)
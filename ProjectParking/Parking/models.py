#unicode: utf-8
from django.db import models

# Create your models here.
class vaga(models.Model):
	numero = models.IntegerField('numero',max_length=2)
	bloco  = models.CharField('bloco',max_length=2)

	def __unicode__(self):
		return u"%d %s"(self.numero,self.bloco)

class carro(models.Model):
	fabricante = models.CharField('fabricante',max_length=20)
	def __unicode__(self):
		return self.fabricante
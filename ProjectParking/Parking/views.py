#encoding:utf-8
from django.shortcuts import render

def index(request):
        context = {'texto': 'Projeto Django no Linux/Ubuntu com Sublime Text 3 avaliação 2'}
        return render(request, 'index.html', context)
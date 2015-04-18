from django.shortcuts import render

def home(request):
        context = {'texto': 'Seu primeiro projeto Django no Linux/Ubuntu com Sublime Text 3'}
        return render(request, 'index.html', context)
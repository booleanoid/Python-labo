from django.shortcuts import render
#from django.http import HttpResponse
#from django.template import loader
from.models import Add_Word

def myapp_index(request):
    data_list = Add_Word.objects.all()
    context = {
        'lists': data_list
    }
    return render(request, 'myapp/index.html', context)

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from.models import Add_Word

# Create your views here.
def index(request):
    data_list = Add_Word.objects.all()
    template = loader.get_template('myapp/index.html')
    context = {
        'lists': data_list
    }
    return HttpResponse(template.render(context, request))

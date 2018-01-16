from django.shortcuts import render
from django.http import HttpResponse
from.models import Add_Word

# Create your views here.
def index(request):
    data_list = Add_Word.objects.all()
    return HttpResponse(data_list)

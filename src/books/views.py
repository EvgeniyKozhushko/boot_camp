from re import T
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def books(request):
    return render(request, template_name='books.html', context={})
    #return render(request, template_name='books.html', context={})

def books_home(request):
    return HttpResponse('HOME')   
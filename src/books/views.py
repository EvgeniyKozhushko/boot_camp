from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy


from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView

from . import models
from . import forms
# Create your views here.

def books_home(request):
    return render(request, template_name ="home.html", context = {})

class HomeBookListView(ListView):
    model = models.Book
    template_name = 'home_books.html'

class BookDetailView(DetailView):
    model = models.Book

class BookCreateView(CreateView):
    model = models.Book
    form_class = forms.CreateBookForm

class BookUpdateView(UpdateView):
    model = models.Book
    form_class = forms.CreateBookForm
    
class BookDeleteView(DeleteView):
    model = models.Book
    success_url = reverse_lazy('home-books')  



class AuthorListView(ListView):
    model = models.Author
    template_name = 'home_authors.html'  

class AuthorDetailView(DetailView):
    model = models.Author    

class AuthorCreateView(CreateView):
    model = models.Author
    form_class = forms.CreateAuthorForm

class AuthorUpdateView(UpdateView):
    model = models.Author
    form_class = forms.CreateAuthorForm
    
class AuthorDeleteView(DeleteView):
    model = models.Author
    success_url = reverse_lazy('home-authors')     
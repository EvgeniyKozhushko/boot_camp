from django import forms
from . import models

class CreateBookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = '__all__'

class CreateAuthorForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = '__all__'        
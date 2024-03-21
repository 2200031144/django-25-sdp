from django import forms
from .models import Book, Category

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'category', 'publication_date']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.

def index(request):

    if request.method == 'POST':
        add_book = BookForm(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()

        add_category = CategoryForm(request.POST)
        if add_category.is_valid():
            add_category.save()

    context = {
        'categories': Category.objects.all(),
        'books': Book.objects.all(),
        'form': BookForm(),
        'formcategory': CategoryForm(),
    }

    return render(request, 'pages/index.html', context)

def books(request):

    context = {
        'categories': Category.objects.all(),
        'books': Book.objects.all(),
    }

    return render(request, 'pages/books.html', context)

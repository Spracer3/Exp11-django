from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from .models import Book
from .forms import BookForm

def home(request):
    books = Book.objects.all()
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'myapp/home.html', {'books': books, 'form': form})

from django.conf import settings
from django.shortcuts import render, get_object_or_404
from .models import Book, BookInstance, Author, Genre

# Create your views here.


def index(request):
    num_books = Book.objects.count()
    num_instances = BookInstance.objects.count()
    num_instances_available = BookInstance.objects.filter(status__exact=0).count()
    num_authors = Author.objects.count()
    num_genres = Genre.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'debug': settings.STATIC_ROOT,
    }

    # return HttpResponse(f"Sveiki atvykę!")
    return render(request, 'library/index.html', context=context)


def authors(request):
    authors = Author.objects.all()
    context = {
        'authors': authors
    }
    return render(request, 'library/authors.html', context=context)


def author(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    return render(request, 'library/author.html', {'author': author})



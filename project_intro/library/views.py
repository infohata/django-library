from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator
from django.conf import settings
from django.db.models import Q
from django.shortcuts import redirect, render, get_object_or_404
from django.views import generic
from django.views.decorators.csrf import csrf_protect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from .models import Book, BookInstance, Author, Genre


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = 'library/user_books.html'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset().filter(current_reader=self.request.user)
        queryset = queryset.filter(status__lte=30).filter(status__gte=10)
        queryset = queryset.order_by('due_back')
        return queryset


class BookListView(generic.ListView):
    model = Book
    template_name = 'libary/book_list.html'
    context_object_name = 'books'
    x = 'Istorija'
    queryset = Book.objects.all()
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        # return queryset.filter(title__icontains=self.x)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'debug': settings.TIME_ZONE})
        return context


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'library/book_detail.html'


def index(request):
    num_books = Book.objects.count()
    num_instances = BookInstance.objects.count()
    num_instances_available = BookInstance.objects.filter(status__exact=0).count()
    num_authors = Author.objects.count()
    num_genres = Genre.objects.count()
    num_visits = int(request.session.get('num_visits', 0)) + 1
    request.session['num_visits'] = num_visits

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'num_visits': num_visits,
        'debug': settings.STATIC_ROOT,
    }

    # return HttpResponse(f"Sveiki atvykę!")
    return render(request, 'library/index.html', context=context)


def authors(request):
    paginator = Paginator(Author.objects.all(), 2)
    page_number = request.GET.get('page')
    paged_authors = paginator.get_page(page_number)
    context = {
        'authors': paged_authors,
        'authors_count': Author.objects.count(),
    }
    return render(request, 'library/authors.html', context=context)


def author(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    return render(request, 'library/author.html', {'author': author})


def search_books(request):
    query = request.GET.get('query')
    search_results = Book.objects.filter(
        Q(title__icontains=query) | 
        Q(summary__icontains=query) | 
        Q(author__last_name__icontains=query)
    )
    context = {
        'books': search_results, 
        'query': query
    }
    return render(request, 'library/search_books.html', context=context)


@csrf_protect
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if not (username and email and password1):
            messages.error(request, _('Incomplete form, all fields are required.'))
        elif password1 != password2:
            messages.error(request, _('Passwords do not match.'))
        elif User.objects.filter(username=username).exists():
            messages.error(request, _('Username already taken.'))
        elif User.objects.filter(email=email).exists():
            messages.error(request, _('User with this email already exists.'))
        else:
            user = User(username=username, email=email)
            user.set_password(password1)
            user.save()
            messages.success(request, _('User registration successful, you can login now.'))
            return redirect(reverse_lazy('login'))
    return render(request, 'library/register.html')

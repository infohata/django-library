from datetime import date, timedelta
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.conf import settings
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from .models import Book, BookInstance, Author, Genre
from .forms import BookReviewForm


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = 'library/user_books.html'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset().filter(current_reader=self.request.user)
        queryset = queryset.filter(status__lte=30).filter(status__gte=10)
        queryset = queryset.order_by('due_back')
        return queryset


class BookByUserCreateView(generic.CreateView, LoginRequiredMixin):
    model = BookInstance
    fields = ['book', 'due_back']
    success_url = reverse_lazy('library:my-books')
    template_name = 'library/user_book_form.html'

    def form_valid(self, form):
        form.instance.current_reader = self.request.user
        form.instance.status = 10
        return super().form_valid(form)

    def get_initial(self):
        initlal = super().get_initial()
        initlal.update({
            'due_back': date.today() + timedelta(days=7)
        })
        return initlal


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


class BookDetailView(generic.DetailView, FormMixin):
    model = Book
    template_name = 'library/book_detail.html'
    context_object_name = 'book'
    form_class = BookReviewForm

    class Meta:
        ordering = ['title']
    

    def get_success_url(self):
        return reverse_lazy('library:book-detail', kwargs={'pk': self.object.id})
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BookReviewForm(initial={
            'book': self.object,
        })
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.book = self.object
        form.instance.reviewer = self.request.user
        form.save()
        return super(BookDetailView, self).form_valid(form)


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

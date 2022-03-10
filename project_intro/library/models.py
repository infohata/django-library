from django.conf import settings
from datetime import date
from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

# Create your models here.

class Genre(models.Model):
    name = models.CharField(_('Name'), max_length=200, 
        help_text=_('ex.: fiction, horror, history, hentai'))

    class Meta:
        ordering = ['name']
        verbose_name = _('Genre')
        verbose_name_plural = _('Genres')

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    title = models.CharField(_('Title'), max_length=200, db_index=True)
    author = models.ForeignKey(
        'Author',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_('Author'),
        related_name='books',
    )
    summary = models.TextField(_('Summary'), max_length=1000, 
        help_text=_('Short description of the book'))
    isbn = models.CharField('ISBN', max_length=13, db_index=True,
        help_text=_('{}ISBN code{}, max 13 symbols').format('<a href="https://www.isbn-international.org/content/what-isbn">', '</a>'))
    genre = models.ManyToManyField(Genre, help_text=_('Select genre(s) for this book'), verbose_name=_('Genre'))
    cover = models.ImageField(_('Cover'), upload_to='covers', null=True)
    

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = _('Book')
        verbose_name_plural = _('Books')


class Author(models.Model):
    first_name = models.CharField(_('Name'), max_length=100, db_index=True)
    last_name = models.CharField(_('Surname'), max_length=100, db_index=True)
    description = models.TextField(_('Description'), max_length=200, blank=True, default='')

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = _('Author')
        verbose_name_plural = _('Authors')

    def __str__(self) -> str:
        return f'{self.last_name} {self.first_name}'


class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, help_text=_('Unique UUID for the exact copy item of the book'))
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, related_name='book_instances')
    due_back = models.DateField(_('Due back'), null=True, blank=True, db_index=True)
    current_reader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    LOAN_STATUS = (
        (0, _('Available')),
        (10, _('Rezerved')),
        (20, _('Taken')),
        (30, _('Unavailable')),
        (50, _('Removed')),
    )

    status = models.PositiveIntegerField(_('Status'), default=0, choices=LOAN_STATUS)

    class Meta:
        ordering = ['due_back']
        verbose_name = _('Book Instance')
        verbose_name_plural = _('Book Instances')
    
    def __str__(self) -> str:
        return f'{self.id} {self.book}'

    @property
    def is_overdue(self):
        if self.status in range(10, 30) and self.due_back and self.due_back < date.today():
            return True
        return False


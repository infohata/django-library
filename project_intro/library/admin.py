from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from .models import Author, Genre, Book, BookInstance

# Register your models here.


class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    fields = ('id', 'status', 'due_back', 'current_reader',)
    readonly_fields = ('id',)
    can_delete = False
    extra = 0


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_author_link', 'get_genres', 'isbn', 'get_instance_counter')
    list_display_links = ('title',)
    list_filter = ('genre',)
    search_fields = ('title', 'author__last_name', 'isbn')
    inlines = (BookInstanceInline,)

    def get_genres(self, obj):
        genres = ', '.join(genre.name for genre in obj.genre.all()[:3])
        if obj.genre.count() > 3:
            return ', '.join([genres, '...'])
        return genres
    get_genres.short_description = _('Genre(s)')

    def get_instance_counter(self, obj):
        return obj.book_instances.count()
    get_instance_counter.short_description = _('Copies')

    def get_author_link(self, obj):
        return format_html('<a href="{}">{}</a>', reverse_lazy('admin:library_author_change', args=[obj.author.id]), obj.author)
    get_author_link.short_description = _('Author')


class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('get_short_id_link', 'get_book_link', 'get_book_author', 'status', 'due_back', 'current_reader', 'is_overdue',)
    list_filter = ('status', 'due_back',)
    search_fields = ('id', 'book__title',)
    readonly_fields = ('id',)

    fieldsets = (
        (None, {
            'fields': ('book', 'id', )
        }),
        (_('Availability'), {
            'fields': ('status', 'due_back', 'current_reader', )
        }),
    )

    def get_book_link(self, obj):
        return format_html('<a href="{}">{}</a>', reverse_lazy('admin:library_book_change', args=[obj.book.id]), obj.book.title)
    get_book_link.short_description = _('Book')

    def get_book_author(self, obj):
        return obj.book.author
    get_book_author.short_description = _('Author')

    def get_short_id_link(self, obj):
        return format_html('<a href="{}">...{}</a>', reverse_lazy('admin:library_bookinstance_change', args=[obj.id]), str(obj.id)[-12:])
    get_short_id_link.short_description = 'ID'


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'get_books',)
    search_fields = ('first_name', 'last_name',)

    def get_books(self, obj):
        books = ', '.join(book.title for book in obj.books.all()[:5])
        if obj.books.count() > 5:
            return ', '.join([books, '...'])
        return books
    get_books.short_description = _('Book(s)')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
admin.site.site_title = _('Library Admin')
admin.site.site_header = _('Library Administration')

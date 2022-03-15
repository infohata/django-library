from django.urls import path

from . import views

app_name = 'library'
urlpatterns = [
    path('', views.index, name='index'),
    path('authors/', views.authors, name='authors'),
    path('authors/<int:author_id>', views.author, name='author'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('books/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('books/search/', views.search_books, name='books-search'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-books'),
    path('mybooks/new/', views.BookByUserCreateView.as_view(), name='my-new-book-instance'),
    path('mybooks/<uuid:pk>/update/', views.BookByUserUpdateView.as_view(), name='update-my-book-instance'),
    path('mybooks/<uuid:pk>/delete/', views.BookByUserDeleteView.as_view(), name='delete-my-book-instance'),
]

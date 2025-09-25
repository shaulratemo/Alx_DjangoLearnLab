from django.urls import path
from .views import (
    BookListView,
    BookCreateView,
    BookDeleteView,
    BookDetailView,
    BookUpdateView
)

urlpatterns = [
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/create/', BookCreateView.as_view(), name='book_create'),
    path('books/update/', BookUpdateView.as_view(), name='book_update'),
    path('books/delete/', BookDeleteView.as_view(), name='book_delete'),
]

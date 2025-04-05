from django.urls import path
from .views import (
    AuthorListView, BookListView, BorrowRecordListView,
    AuthorCreateView, BookCreateView, BorrowRecordCreateView,
    export_to_excel, home_view
)

urlpatterns = [
    path('', home_view, name='home'),
    path('authors/', AuthorListView.as_view(), name='author_list'),
    path('authors/add/', AuthorCreateView.as_view(), name='author_add'),
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/add/', BookCreateView.as_view(), name='book_add'),
    path('borrow-records/', BorrowRecordListView.as_view(), name='borrowrecord_list'),
    path('borrow-records/add/', BorrowRecordCreateView.as_view(), name='borrowrecord_add'),
    path('export/', export_to_excel, name='export_to_excel'),
]
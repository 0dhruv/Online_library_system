from django.contrib import admin
from .models import Author, Book, BorrowRecord

# Remove any duplicate @admin.register decorators or admin.site.register() calls
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'bio')
    search_fields = ('name', 'email')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'published_date', 'author')
    list_filter = ('genre', 'published_date')
    search_fields = ('title', 'author__name')

@admin.register(BorrowRecord)
class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'book', 'borrow_date', 'return_date')
    list_filter = ('borrow_date', 'return_date')
    search_fields = ('user_name', 'book__title')
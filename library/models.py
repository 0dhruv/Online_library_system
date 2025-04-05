from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, validators=[validate_email])
    bio = models.TextField()

    def __str__(self):
        return self.name

    def clean(self):
        super().clean()
        try:
            validate_email(self.email)
        except ValidationError:
            raise ValidationError({'email': 'Please enter a valid email address.'})

class Book(models.Model):
    GENRE_CHOICES = [
        ('FIC', 'Fiction'),
        ('NF', 'Non-Fiction'),
        ('SF', 'Science Fiction'),
        ('FAN', 'Fantasy'),
        ('BIO', 'Biography'),
        ('HIS', 'History'),
        ('OTH', 'Other'),
    ]
    
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=3, choices=GENRE_CHOICES, default='FIC')
    published_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} by {self.author.name}"

class BorrowRecord(models.Model):
    user_name = models.CharField(max_length=100)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user_name} borrowed {self.book.title}"
from django.db import models

# Create your models here.
# Author model representing a book author
class Author(models.Model):
    name = models.CharField(max_length=100)
    
# Book model representing a single book
# Each book belongs to one author
class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
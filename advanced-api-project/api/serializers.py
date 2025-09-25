from rest_framework import serializers
from .models import Author, Book
from datetime import date

# Serializer for Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']
        
    # Includes validation ot ensure publication_year is not in the future
    def validate_publication_year(self, value):
        current_year = date.today().year
        
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be n the future.")
        return value

# Serializer for Author model
# Nests BookSerializer to show all books written by an author
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    
    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
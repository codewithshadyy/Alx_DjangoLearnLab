from .models import Author, Book
from rest_framework import serializers
from datetime import datetime

        
class BookSerializer(serializers.ModelSerializer):
    """
    Serializes Book model fields.
    Includes custom validation to ensure the publication year
    is not set in the future.
    """
    
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author[name]']
        
    def validate_publication(self, value):
        
        """
        Ensure publication year is not greater than the current year.
        """
        
        current_year = datetime.now().year
        if value > current_year:
            serializers.ValidationError("Publication year cannot be in the future")    
        

class AuthorSerializer(serializers.ModelSerializer):
    
    """
    Serializes Author model.
    Includes a nested representation of related books using
    BookSerializer.
    """
    
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model =  Author
        fields = ['id', 'name', 'books']              

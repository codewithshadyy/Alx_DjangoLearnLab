from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Book
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend
from  django_filters import rest_framework

# ListView - Retrieves all  books

class BookListView(generics.ListAPIView):
    
    """
    Integrate Django REST Framework’s filtering capabilities to allow users to filter the book list by various attributes like title, author, and publication_year.”


    """
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]
    
    filter_backends  = [
        rest_framework.DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]
    
      # Filtering configuration
    filterset_fields = ['title', 'publication_year', 'author']

    # Search configuration
    search_fields = ['title', 'author__name']

    # Ordering configuration
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']
    
    
    
      
    
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
       
        print(f"Creating book: {serializer.validated_data['title']}")
        serializer.save()
        
    
    
# DetailView - retrieves single book by ID  
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]

# UpdateView - modifies existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]            

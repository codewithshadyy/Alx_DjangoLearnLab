from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


# ListView - Retrieves all  books

class BookListView(generics.ListAPIView):
    
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_queryset(self):
        """
        Optionally filter by author name using query param ?author=Name
        """
        queryset = Book.objects.all()
        author_name = self.request.query_params.get('author')
        if author_name:
            queryset = queryset.filter(author__name__icontains=author_name)
        return queryset    
        
    
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
       
        print(f"Creating book: {serializer.validated_data['title']}")
        serializer.save()
        
    
    
# DetailView - retrieves single book by ID  
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# UpdateView - modifies existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]            

from django.shortcuts import render
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment
from .permissions import IsOwner
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['title', 'content']
    
    def perform_create(self, serializer):
         serializer.save(author=self.request.user)
    
class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)   
        
        
        
         

# APi Endpoint         
         
         
#  GET     /api/posts/
# POST    /api/posts/
# GET     /api/posts/{id}/
# PUT     /api/posts/{id}/
# DELETE  /api/posts/{id}/

# GET     /api/comments/
# POST    /api/comments/
# ...
        


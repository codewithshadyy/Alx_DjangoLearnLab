from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment
from .permissions import IsOwner
from rest_framework import viewsets, generics, permissions
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['title', 'content']
    
    def perform_create(self, serializer):
         serializer.save(author=self.request.user)
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user) 
        


class FeedView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        following_users = request.user.following.all()

        posts = Post.objects.filter(author__in=following_users).order_by("-created_at")

        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)         
        
        
        
         

# APi Endpoint         
         
         
#  GET     /api/posts/
# POST    /api/posts/
# GET     /api/posts/{id}/
# PUT     /api/posts/{id}/
# DELETE  /api/posts/{id}/

# GET     /api/comments/
# POST    /api/comments/
# ...
        


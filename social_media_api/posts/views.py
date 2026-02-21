from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment, Like
from .permissions import IsOwner
from rest_framework import viewsets, generics, permissions, status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType

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
        
        
        
#  API Endpoint for liking and unliking post
class LikePostView(generics.GenericAPIView):
       permission_classes = [permissions.IsAuthenticated]
       
       def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)

        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if not created:
            return Response(
                {"detail": "You already liked this post."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Creating da notification
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb="liked your post",
            content_type=ContentType.objects.get_for_model(post),
            object_id=post.id,
        )

        return Response({"detail": "Post liked."}, status=200)
    
    
class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)

        like = Like.objects.filter(user=request.user,post=post)

        if not like.exists():
            return Response(
                {"detail": "You have not liked this post."},
                status=status.HTTP_400_BAD_REQUEST
            )

        like.delete()

        return Response({"detail": "Post unliked."}, status=200)    





# APi Endpoint  for post and comment model       
         
         
#  GET     /api/posts/
# POST    /api/posts/
# GET     /api/posts/{id}/
# PUT     /api/posts/{id}/
# DELETE  /api/posts/{id}/

# GET     /api/comments/
# POST    /api/comments/
# ...
        

# What Happens Now
# When a user:
# Action	Result
# Likes post	Like created + Notification generated
# Unlikes post	Like removed
# Fetch notifications	Gets newest first
# Already liked	Blocked
# Not authenticated	Blocked
#  Example API Calls
# Like Post
# POST /posts/3/like/
# Authorization: Token <token>
# Unlike Post
# POST /posts/3/unlike/
# View Notifications
# GET /notifications/v
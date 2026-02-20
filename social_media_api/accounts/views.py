from rest_framework  import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.decorators  import permission_classes, api_view
from rest_framework import status


from .models import User
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer

class RegisterView(generics.CreateAPIView):
     queryset = User.objects.all()
     serializer_class = RegisterSerializer
     
class LoginView(APIView):
    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
    
        return Response({
            'user': serializer.validated_data['user'].username,
            'token': serializer.validated_data['token']
        })
        
class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user                 


# implementing follow and unfollow view

@api_view(["POST"])
@permission_classes([IsAuthenticated])

def follow_user(request, user_id):
    
    try:
        user_to_follow = User.Objects.get(id=user_id)
        
    except User.DoesNotExist:
        return Response({"error":"user not found"}, status=status.HTTP_404_NOT_FOUND)  
    
    if request.user == request.user_to_follow:  
        return Response({"error":"tou cannot follow yourself"}, status=status.HTTP_400_BAD_REQUEST)
    
    request.user.following.add(user_to_follow)
    
    
    return Response({"message": f"You are now following {user_to_follow.username}"})


@api_view(["POST"])
@permission_classes([IsAuthenticated])

def unfollow_user(request, user_id):
    try:
        user_to_unfollow = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    request.user.following.remove(user_to_unfollow)

    return Response({"message": f"You have unfollowed {user_to_unfollow.username}"})

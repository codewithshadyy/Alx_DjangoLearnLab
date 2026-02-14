
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Post, Comment

class CustomUserCreation(UserCreationForm):
    email = forms.EmailField(required= True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']  
        
        
        
# cretaing post form


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        
        
#creating a comment form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content'] 
        
           
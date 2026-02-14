
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Post, Comment, Tag

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
        
           
           
 #  creating a tag form
 
class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text="Enter tags separated by commas")

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()

        tags_data = self.cleaned_data['tags']
        if tags_data:
            tag_names = [tag.strip() for tag in tags_data.split(',')]
            for tag_name in tag_names:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                instance.tags.add(tag)

        return instance  
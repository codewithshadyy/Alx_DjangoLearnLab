from django.shortcuts import render, redirect

from .forms import CustomUserCreation, UserUpdateForm
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, aauthenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin





def register_view(request):
    
    if request.method == "POST":
        form  = CustomUserCreation(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "registration succesful")
        else:
            messages.error(request, "Please correct the error below.")    
    else:
         form = CustomUserCreation()
    return render(request, 'blog/register.html', {'form': form})


@login_required
def profile_view(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('profile')
        else:
            messages.error(request, "Please correct the error below.")
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'blog/profile.html', {'form': form})





# List all posts (Public)
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-published_date']


#  View single post (Public)
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


#  Create post (Only logged-in users)
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# Update post (Only author)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


#  Delete post (Only author)
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


from django.shortcuts import render, redirect

from .forms import CustomUserCreation, UserUpdateForm
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, aauthenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages





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


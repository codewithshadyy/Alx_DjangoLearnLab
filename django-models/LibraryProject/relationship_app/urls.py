from django.urls import path
from . import views
from .views import list_books

urlpatterns = [
    # Function-based view
    path('books/', views.list_books, name='list_books'),

    # Class-based view
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]

from django.shortcuts import render
from django.contrib.auth.models import Group, Permission
from bookshelf.models import Book
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from bookshelf.models import Book
from django.forms import BookForm
from bookshelf.forms import BookSearchForm

# Create your views here.







# View to create a book
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/book_form.html', {'form': form})

# View to edit a book
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/book_form.html', {'form': form})

# View to delete a book
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')

# View to view a book
@permission_required('bookshelf.can_view', raise_exception=True)
def view_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'bookshelf/book_detail.html', {'book': book})


# searching book
def book_search(request):
    form = BookSearchForm(request.GET or None)
    books = Book.objects.none()  # default empty queryset
    if form.is_valid():
        title_query = form.cleaned_data['title']
        books = Book.objects.filter(title__icontains=title_query)  # ORM prevents SQL injection
    return render(request, 'bookshelf/book_list.html', {'form': form, 'books': books})


# settings.py
# DEBUG is False in production for security
# SECURE_BROWSER_XSS_FILTER prevents reflected XSS attacks
# X_FRAME_OPTIONS = 'DENY' prevents clickjacking
# CSRF_COOKIE_SECURE ensures CSRF cookie sent over HTTPS only


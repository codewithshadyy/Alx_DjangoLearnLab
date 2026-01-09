
# CRUD Operations for Book model

## Create
```python
from bookshelf.models import Book
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()  # Book instance created



book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year
# Output: ('1984', 'George Orwell', 1949)


book.title = "Nineteen Eighty-Four"
book.save()
Book.objects.get(id=book.id).title
# Output: 'Nineteen Eighty-Four'


book.delete()
Book.objects.all()
# Output: <QuerySet []>

API Endpoints:

GET    /api/books/             → List all books
GET    /api/books/<id>/        → Retrieve a single book
POST   /api/books/create/      → Create a new book (authenticated)
PATCH  /api/books/<id>/update/ → Update a book (authenticated)
DELETE /api/books/<id>/delete/ → Delete a book (authenticated)

Permissions:

- List & Detail: open to all
- Create, Update, Delete: requires authentication

Custom Features:

- BookSerializer validates publication_year
- BookListView supports optional ?author=Name filtering





### Advanced Query Features

The Book list endpoint supports filtering, searching, and ordering.

#### Filtering
- Filter by title:
  /api/books/?title=Clean Code
- Filter by publication year:
  /api/books/?publication_year=2021
- Filter by author ID:
  /api/books/?author=1

#### Search
- Search by title or author name:
  /api/books/?search=django

#### Ordering
- Order by title:
  /api/books/?ordering=title
- Order by publication year (descending):
  /api/books/?ordering=-publication_year

#### Combined Queries
- Example:
  /api/books/?search=python&ordering=-publication_year

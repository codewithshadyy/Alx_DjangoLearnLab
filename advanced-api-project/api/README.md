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

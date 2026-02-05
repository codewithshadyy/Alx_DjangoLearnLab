from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Author, Book




class BookAPITestCase(APITestCase):
    
     """
    Test suite for Book API endpoints.
    Covers CRUD operations, filtering, searching,
    ordering, and permission enforcement.
    """
    
     def setUp(self):
        """
        Set up test data before each test runs.
        """
        self.author = Author.objects.create(name="Test Author")

        self.book1 = Book.objects.create(
            title="Django for Beginners",
            publication_year=2020,
            author=self.author
        )

        self.book2 = Book.objects.create(
            title="Advanced Django",
            publication_year=2022,
            author=self.author
        )

        self.user = User.objects.create_user(
            username="testuser",
            password="password123"
        )

        self.list_url = "/api/books/"
        self.create_url = "/api/books/create/"

    # -----------------------------
    # READ OPERATIONS
    # -----------------------------

     def test_list_books(self):
        """
        Test retrieving the list of books.
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

     def test_retrieve_single_book(self):
        """
        Test retrieving a single book by ID.
        """
        url = f"/api/books/{self.book1.id}/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book1.title)

    # -----------------------------
    # CREATE OPERATION
    # -----------------------------

     def test_create_book_authenticated(self):
        """
        Test creating a book as an authenticated user.
        """
        self.client.login(username="testuser", password="password123")

        data = {
            "title": "New Django Book",
            "publication_year": 2021,
            "author": self.author.id
        }

        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

     def test_create_book_unauthenticated(self):
        """
        Test creating a book without authentication.
        """
        data = {
            "title": "Unauthorized Book",
            "publication_year": 2021,
            "author": self.author.id
        }

        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # -----------------------------
    # UPDATE OPERATION
    # -----------------------------

     def test_update_book_authenticated(self):
        """
        Test updating a book as an authenticated user.
        """
        self.client.login(username="testuser", password="password123")

        url = f"/api/books/{self.book1.id}/update/"
        data = {"title": "Updated Django Title"}

        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Django Title")

    # -----------------------------
    # DELETE OPERATION
    # -----------------------------

     def test_delete_book_authenticated(self):
        """
        Test deleting a book as an authenticated user.
        """
        self.client.login(username="testuser", password="password123")

        url = f"/api/books/{self.book1.id}/delete/"
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # -----------------------------
    # FILTERING, SEARCHING, ORDERING
    # -----------------------------

     def test_filter_books_by_publication_year(self):
        """
        Test filtering books by publication year.
        """
        response = self.client.get(self.list_url + "?publication_year=2022")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Advanced Django")

     def test_search_books_by_title(self):
        """
        Test searching books by title.
        """
        response = self.client.get(self.list_url + "?search=Advanced")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

     def test_order_books_by_publication_year(self):
        """
        Test ordering books by publication year.
        """
        response = self.client.get(self.list_url + "?ordering=-publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data[0]["publication_year"],
        )
        
        

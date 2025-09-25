from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Author, Book


class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username="tester", password="pass123")

        # Create an author
        self.author = Author.objects.create(name="John Doe")

        # Create a book
        self.book = Book.objects.create(
            title="First Book",
            publication_year=2020,
            author=self.author
        )

        # Define URLs
        self.list_url = "/api/books/"
        self.detail_url = f"/api/books/{self.book.id}/"
        self.create_url = "/api/books/create/"
        self.update_url = f"/api/books/update/"
        self.delete_url = f"/api/books/delete/"

    # ----------- CRUD TESTS -----------

    def test_list_books(self):
        """Anyone can list books"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_retrieve_book(self):
        """Anyone can retrieve a single book"""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book.title)

    def test_create_book_unauthenticated(self):
        """Unauthenticated users cannot create books"""
        response = self.client.post(self.create_url, {
            "title": "Unauthorized Book",
            "publication_year": 2021,
            "author": self.author.id
        })
        self.assertIn(response.status_code, [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN])

    def test_create_book_authenticated(self):
        """Authenticated users can create books"""
        self.client.login(username="tester", password="pass123")
        response = self.client.post(self.create_url, {
            "title": "Authorized Book",
            "publication_year": 2021,
            "author": self.author.id
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_update_book_authenticated(self):
        """Authenticated users can update a book"""
        self.client.login(username="tester", password="pass123")
        response = self.client.put(self.update_url, {
            "title": "Updated Book",
            "publication_year": 2022,
            "author": self.author.id
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book")

    def test_delete_book_authenticated(self):
        """Authenticated users can delete a book"""
        self.client.login(username="tester", password="pass123")
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    # ----------- FILTERING, SEARCHING, ORDERING -----------

    def test_filter_books_by_year(self):
        response = self.client.get(self.list_url, {"publication_year": 2020})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "First Book")

    def test_search_books_by_title(self):
        response = self.client.get(self.list_url, {"search": "First"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "First Book")

    def test_order_books_by_year_desc(self):
        Book.objects.create(
            title="Second Book",
            publication_year=2025,
            author=self.author
        )
        response = self.client.get(self.list_url, {"ordering": "-publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(response.data[0]["publication_year"], response.data[1]["publication_year"])
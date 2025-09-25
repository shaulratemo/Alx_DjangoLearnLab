from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer

# Create your views here.
# BookListView:
# - Provides a list of all Book objects in the database.
# - Uses GET requests.
# - Accessible to all users (AllowAny).
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# BookDetailView:
# - Retrieves a single Book instance by its primary key (id).
# - Uses GET requests.
# - Accessible to all users (AllowAny).
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# BookCreateView:
# - Allows creation of new Book objects.
# - Uses POST requests.
# - Restricted to authenticated users only.
# - Custom hook: perform_create() is included so that
#   additional logic can be added (e.g., associating the book with request.user).
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save()

# BookUpdateView:
# - Allows updating of existing Book objects.
# - Uses PUT/PATCH requests.
# - Restricted to authenticated users only.
# - Custom hook: perform_update() is included to allow custom behavior
#   when saving an update (e.g., enforcing rules on who can update).
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_update(self, serializer):
        serializer.save()

# BookDeleteView:
# - Allows deletion of existing Book objects.
# - Uses DELETE requests.
# - Restricted to authenticated users only.
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
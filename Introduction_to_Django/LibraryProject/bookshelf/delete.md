from bookshelf.models import Book
book = Book.objects.get(id=3)
book.delete()
(1, {'bookshelf.Book': 1})
Book.objects.all()
<QuerySet []>
book = Book.objects.get(id=3) 
book.title = "Nineteen Eighty-Four"
book.save()
book
<Book: Nineteen Eighty-Four by George Orwell published in 1949>
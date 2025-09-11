# Django Admin Interface for Book Model

## Creating the superuser
Command:
```bash
python manage.py createsuperuser

Username: admin
Email address: admin@example.com
Password:
Password (again):
Superuser created successfully.
```
## Registration
In 'bookshelf/admin.py', the Book model was registered with these customizations:
```python
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('publication_year', 'author') 
    search_fields = ('title', 'author')

admin.site.register(Book, BookAdmin)
```
## Running server
```bash
python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
August 28, 2025 - 18:31:43
Django version 5.2.5, using settings 'LibraryProject.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
Open http://127.0.0.1:8000/admin
Log in using the superuser credentials.
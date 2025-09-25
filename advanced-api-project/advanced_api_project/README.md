## View Configurations

- **BookListView**  
  Retrieves all books (GET). Accessible to all users.

- **BookDetailView**  
  Retrieves a single book by its ID (GET). Accessible to all users.

- **BookCreateView**  
  Creates a new book (POST). Restricted to authenticated users.  
  Custom hook: `perform_create()` is used to allow custom logic when creating.

- **BookUpdateView**  
  Updates an existing book (PUT/PATCH). Restricted to authenticated users.  
  Custom hook: `perform_update()` allows extending behavior during updates.

- **BookDeleteView**  
  Deletes an existing book (DELETE). Restricted to authenticated users.
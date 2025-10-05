# Blog Post Management

## Overview
This section adds full CRUD functionality for blog posts. Authenticated users can create, edit, and delete posts, while anyone can view all posts.

## Features
- **ListView:** Displays all blog posts.
- **DetailView:** Shows a single post in full.
- **CreateView:** Allows logged-in users to publish posts.
- **UpdateView:** Restricts editing to the post’s author.
- **DeleteView:** Restricts deletion to the post’s author.

## Permissions
- Authenticated users can create posts.
- Only the post author can edit or delete.
- Unauthenticated users can view posts but cannot modify them.

## URLs
- `/posts/` — list all posts
- `/posts/new/` — create a new post
- `/posts/<id>/` — view post details
- `/posts/<id>/edit/` — edit post
- `/posts/<id>/delete/` — delete post

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

# Comment System

## Overview
Adds a comment feature allowing users to discuss posts.

## Features
- Authenticated users can add comments.
- Only comment authors can edit or delete their comments.
- Comments are displayed under each blog post.

## URLs
- `/posts/<post_id>/comments/new/` — add a new comment
- `/comments/<comment_id>/edit/` — edit an existing comment
- `/comments/<comment_id>/delete/` — delete a comment

## Permissions
- Authenticated users can comment.
- Only comment authors can edit or delete their own comments.


# Tagging and Search Functionality

## Overview
This feature allows users to organize and find posts easily using tags and keyword search.

## Features
- **Tagging:** Users can add multiple tags to posts.
- **Tag Filter:** Click any tag to view all posts under it.
- **Search:** Search for posts by title, content, or tags.

## URLs
- `/tags/<tag_name>/` — View all posts with a specific tag.
- `/search/?q=keyword` — Search posts by keyword.

## Example
1. Add tags when creating or editing a post (e.g., “django, backend, API”).
2. Use the search bar to find posts by keyword.
3. Click a tag to explore all posts under that tag.

### Social Media API – User Authentication
### Overview

This project is the foundation of a Django-based Social Media API.
It sets up a user authentication system using Django REST Framework and token authentication.
Users can register, log in, and manage their profiles securely.

### Features

User registration with username, email, and password

User login and token generation

User profile view and update

Secure authentication using Django REST Framework’s token authentication

Custom user model with bio, profile picture, and followers field

### Setup Instructions
1. Clone the Repository
git clone https://github.com/<your-username>/Alx_DjangoLearnLab.git
cd Alx_DjangoLearnLab/social_media_api

2. Create and Activate Virtual Environment
python -m venv .venv
source .venv/Scripts/activate  # For Git Bash on Windows

3. Install Dependencies
pip install django djangorestframework djangorestframework-simplejwt

4. Apply Migrations
python manage.py makemigrations
python manage.py migrate

5. Run the Development Server
python manage.py runserver

### API Endpoints
Endpoint	Method	Description
/api/register/	POST	Register a new user
/api/login/	POST	Log in and retrieve authentication token
/api/profile/	GET, PUT	Retrieve or update user profile (requires token)
Example Requests
Register
POST /api/register/
{
  "username": "john",
  "email": "john@example.com",
  "password": "12345"
}

Login
POST /api/login/
{
  "username": "john",
  "password": "12345"
}


Response:

{
  "token": "generated_token_here",
  "user": {
    "id": 1,
    "username": "john",
    "email": "john@example.com"
  }
}

Profile (Authenticated)

Header:

Authorization: Token your_token_here

GET /api/profile/


Response:

{
  "id": 1,
  "username": "john",
  "email": "john@example.com",
  "bio": "",
  "profile_picture": null,
  "followers": []
}

## Posts & Comments API

POST /api/posts/ – create post

GET /api/posts/ – list posts (supports search & ordering)

GET /api/posts/{id}/ – view post with nested comments

POST /api/comments/ – add a comment to a post

Permissions: only authors may edit/delete their own content

### Custom User Model

The custom user model extends Django’s AbstractUser and includes:

bio: A short description about the user

profile_picture: Optional user profile image

followers: A self-referential ManyToManyField for following other users

To reference it, AUTH_USER_MODEL is set as:

AUTH_USER_MODEL = 'accounts.User'

### Authentication

This project uses Token Authentication via:

'DEFAULT_AUTHENTICATION_CLASSES': [
    'rest_framework.authentication.TokenAuthentication',
]


Tokens are automatically generated upon registration or login.

### Testing

You can use Postman or curl to test:

Register a new user.

Log in with credentials to get a token.

Use that token to access or update the profile endpoint.

Directory Structure
social_media_api/
├── accounts/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
├── social_media_api/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
├── manage.py

## Follows & Feed

### Follow / Unfollow
- POST /api/accounts/follow/<user_id>/ — follow the target user (authenticated)
- POST /api/accounts/unfollow/<user_id>/ — unfollow the target user (authenticated)

### Followers / Following lists
- GET /api/accounts/users/<user_id>/followers/ — list followers of the user
- GET /api/accounts/users/<user_id>/following/ — list users the user follows

### Feed
- GET /api/feed/ — returns posts by users you follow, ordered newest first (authenticated)

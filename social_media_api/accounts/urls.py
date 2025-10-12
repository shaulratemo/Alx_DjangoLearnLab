from django.urls import path
from .views import RegisterView, LoginView, ProfileView
from . import views

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('follow/<int:user_id>/', views.follow_user, name='follow_user'),
    path('unfollow/<int:user_id>/', views.unfollow_user, name='unfollow_user'),
    path('users/<int:pk>/following/', views.FollowingListView.as_view(), name='user_following'),
    path('users/<int:pk>/followers/', views.FollowersListView.as_view(), name='user_followers'),
]

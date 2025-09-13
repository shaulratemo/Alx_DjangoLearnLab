from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("username", "email", "date_of_birth", "profile_photo")
        
class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)
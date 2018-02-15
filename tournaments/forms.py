from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import User, Profile, Tourney

class UserForm(UserCreationForm):
    wins = forms.IntegerField(min_value=0, max_value=5)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'wins')


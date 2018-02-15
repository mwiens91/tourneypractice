from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import User, Profile, Tourney

class UserForm(UserCreationForm):
    wins = forms.IntegerField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'wins')


from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Tourney, Profile, User
from .forms import UserForm

@login_required
def home(request):
    tourney_list = Tourney.objects.order_by('-id')
    context = {'tourney_list': tourney_list}
    return render(request, 'home.html', context)

@login_required
def tourney(request,tourney_id):
    thistourney = Tourney.objects.get(id=tourney_id)
    numplayers = thistourney.player.count()
    return render(request,'tourney.html', {'tourney': thistourney,
                                            'numplayers': numplayers})
def logout_view(request):
    logout(request)

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.wins =form.cleaned_data.get('wins')
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

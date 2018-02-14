from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Tourney

@login_required
def home(request):
    tourney_list = Tourney.objects.order_by('-id')
    context = {'tourney_list': tourney_list}
    return render(request, 'home.html', context)

def tourney(request,tourney_id):
    thistourney = Tourney.objects.get(id=tourney_id)
    numplayers = thistourney.player.count()
    return render(request,'tourney.html', {'tourney': thistourney,
                                            'numplayers': numplayers})


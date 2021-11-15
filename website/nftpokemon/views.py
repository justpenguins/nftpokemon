from types import NoneType
from django.shortcuts import render
from .algorithm import get_stats
from .models import NFT
from .battle import round
import os

from requests.api import get
from .nfts import get_random_nft

# Create your views here.
def index(request):

    context = {"nfts": NFT.objects.all()}

    return render(request, 'home.html', context)

def battle(request):
    player = NFT.objects.get(token=277)

    enemy = get_random_nft()
    while enemy is NoneType:
        enemy = get_random_nft()

    n = NFT(name = enemy['name'], token = int(enemy['token']), img = enemy['image'], hash = enemy['hash'])
    n.save()

    enemy['stats'] = get_stats(enemy['hash'])

    result = round(player.hash, enemy['hash'])
    

    context = {'player': player, 'player_stats': get_stats(player.hash), 'enemy': enemy, "result": result}

    return render(request, 'battle.html', context)

def battleknown(request, address, token_id):
    
    context = {}
    return render(request, 'battle.html', context)
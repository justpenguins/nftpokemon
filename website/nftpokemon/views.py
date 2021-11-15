from types import NoneType
from django.shortcuts import render
from .models import NFT
import os

from requests.api import get
from .nfts import get_random_nft

# Create your views here.
def index(request):

    context = {"nfts": NFT.objects.all()}

    return render(request, 'home.html', context)

def battle(request):
    temp = get_random_nft()
    while temp is NoneType:
        temp = get_random_nft()
    print(temp)
    n = NFT(name = temp['name'], token = int(temp['token']), img = temp['image'], hash = temp['hash'])
    n.save()

    context = temp

    return render(request, 'battle.html', context)

def battleknown(request, address, token_id):
    
    context = {}
    return render(request, 'battle.html', context)
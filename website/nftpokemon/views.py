from types import NoneType
from django.shortcuts import render
import os

from requests.api import get
from .nfts import get_random_nft

# Create your views here.
def index(request):

    context = {}

    return render(request, 'home.html', context)

def battle(request):
    print(os.getcwd())
    temp = get_random_nft()
    while temp is NoneType:
        temp = get_random_nft()


    print(temp)
    context = temp

    return render(request, 'battle.html', context)

def battleknown(request, address, token_id):
    
    context = {}
    return render(request, 'battle.html', context)
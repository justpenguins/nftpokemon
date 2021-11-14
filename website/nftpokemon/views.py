from django.shortcuts import render

# Create your views here.
def index(request):

    context = {}

    return render(request, 'index.html', context)

def battle(request, summoner_name):
    
    context = {}
    return render(request, 'summoner_detail.html', context)
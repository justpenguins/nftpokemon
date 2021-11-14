from django.shortcuts import render

# Create your views here.
def index(request):
    directory = 'summoner_info/ranked_info/'
    summoners = []
    summoner_names = []

    context = {'summoner_names': summoner_names, 'summoner_stats': summoners}

    return render(request, 'index.html', context)

def display_summoner(request, summoner_name):
    directory = 'summoner_info/ranked_info/'
    summoner_stats = json.load(open(directory + summoner_name + ".json"))

    context = {'name': summoner_name, 'summoner_stats': summoner_stats}

    return render(request, 'summoner_detail.html', context)
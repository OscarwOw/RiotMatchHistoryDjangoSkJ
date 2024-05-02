# polls/views/index.py
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def summonerView(request, summonername="W1S OscarwOw", summonerDetail=None):
    if summonerDetail is not None:
        print(summonerDetail)
        context = {
            'summonername': summonername,
            'summoner': summonerDetail['summoner'],
            'soloQ': summonerDetail['summonerentries']['soloQ'], #TODO fix context so that it handles if no data found
            'flexQ': summonerDetail['summonerentries']['flexQ']
        }
    else:
        context = {
            'summonername': summonername,
            'error': "No summoner data available"
        }
    return render(request, 'summoner.html', context)

def summonerNotFoundView(request, summonername):
    return render(request, 'summonerNotFound.html', {"name": summonername})

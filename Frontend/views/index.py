# polls/views/index.py
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def summonerView(request, summonername, summonerDetail=None, server='eune'):
    if summonerDetail is not None:
        print(f"summoner derail: {summonerDetail}")
        context = {
            'server': server,
            'summonername': summonername,
            'summonerdetail': summonerDetail,
            'summoner': summonerDetail['summoner'],
            #'soloQ': summonerDetail,#['summonerentries']['soloQ'], #TODO fix context so that it handles if no data found
            #'flexQ': summonerDetail['summonerentries']['flexQ']
        }
    else:
        context = {
            'summonername': summonername,
            'error': "No summoner data available"
        }
    return render(request, 'summoner.html', context)

def matchHistoryView(request, summonername="W1S OscarwOw", matchhistory=None, summonerid=None):
    if matchhistory is not None:


        context = {'summonername': summonername, 'matches': matchhistory['matches'][0], 'summonerid': summonerid}
    else:
        context = {
            'summonername': summonername,
            'error': "No summoner data available"
        }
    return render(request, 'matchhistory.html', context)


def summonerNotFoundView(request, summonername):
    return render(request, 'summonerNotFound.html', {"name": summonername})

def matchNotFoundView(request, id):
    return render(request, 'matchNotFound.html', {"id": id})

def matchDetailView(request, match, server):
    context = {'match': match,
               'blue_team_range': range(0, 5),  # Zero-based indices for JavaScript
               'red_team_range': range(5, 10),
               }
    print(f"works2")
    return render(request, 'matchDetail.html', context)

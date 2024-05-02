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

def matchHistoryView(request, summonername="W1S OscarwOw", matchhistory=None):
    if matchhistory is not None:
        print(matchhistory)
        context = {
            'summonername': summonername,
            'participant1': matchhistory['metadata']['participants'][0]['account']['gameName'],
            'participant2': matchhistory['metadata']['participants'][1]['account']['gameName'],
            'participant3': matchhistory['metadata']['participants'][2]['account']['gameName'],
            'participant4': matchhistory['metadata']['participants'][3]['account']['gameName'],
            'participant5': matchhistory['metadata']['participants'][4]['account']['gameName'],
            'participant6': matchhistory['metadata']['participants'][5]['account']['gameName'],
            'participant7': matchhistory['metadata']['participants'][6]['account']['gameName'],
            'participant8': matchhistory['metadata']['participants'][7]['account']['gameName'],
            'participant9': matchhistory['metadata']['participants'][8]['account']['gameName'],
            'participant10': matchhistory['metadata']['participants'][9]['account']['gameName']

        }
    else:
        context = {
            'summonername': summonername,
            'error': "No summoner data available"
        }
    return render(request, 'matchhistory.html', context)


def summonerNotFoundView(request, summonername):
    return render(request, 'summonerNotFound.html', {"name": summonername})

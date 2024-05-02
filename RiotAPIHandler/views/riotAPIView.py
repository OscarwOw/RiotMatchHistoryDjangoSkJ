from ..utils import FetchSummoner, FetchSummonerLeagueEntry, FetchSummonerMatchHistory
from Frontend.views import summonerView, summonerNotFoundView, matchHistoryView


async def summonerProfile(request, summonername):
    summonerdetail = {}
    summonerdetail['summoner'] = await FetchSummoner(summonername)



    if(summonerdetail['summoner'] == None):
        print('dear lord')
        return summonerNotFoundView(request, summonername)

    summonerdetail['summonerentries'] = await FetchSummonerLeagueEntry(summonerdetail['summoner'].summonerId)
    return summonerView(request, summonername, summonerdetail)

async def summonerMatchHistory(request, summonername):
    matchhistory = {}
    summoner = await FetchSummoner(summonername)
    matchhistoryFetch = await FetchSummonerMatchHistory(summoner.puuid)

    matchhistory['matches'] = []
    matchhistory['matches'].append(matchhistoryFetch)
    #matchhistory['summonername']
    return matchHistoryView(request, summonername, matchhistory)

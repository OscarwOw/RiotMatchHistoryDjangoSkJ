from ..utils import FetchSummoner, FetchSummonerLeagueEntry, FetchSummonerMatchHistory
from Frontend.views import summonerView, summonerNotFoundView


async def summonerProfile(request, summonername):
    summonerdetail = {}
    summonerdetail['summoner'] = await FetchSummoner(summonername)
    matchhistory = await FetchSummonerMatchHistory(summonerdetail['summoner'].puuid)


    if(summonerdetail['summoner'] == None):
        print('dear lord')
        return summonerNotFoundView(request, summonername)

    summonerdetail['summonerentries'] = await FetchSummonerLeagueEntry(summonerdetail['summoner'].summonerId)
    return summonerView(request, summonername, summonerdetail)
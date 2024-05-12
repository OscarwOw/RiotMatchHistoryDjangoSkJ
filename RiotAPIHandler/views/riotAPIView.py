from ..utils import FetchSummoner, FetchSummonerLeagueEntry, FetchSummonerMatchHistory, FetchMatch
from Frontend.views import summonerView, summonerNotFoundView, matchHistoryView, matchDetailView, matchNotFoundView


async def summonerProfile(request, summonername, server):
    summonerdetail = {}
    summonerdetail['summoner'] = await FetchSummoner(summonername, server)

    if(summonerdetail['summoner'] == None):
        print("summoner not found")
        return summonerNotFoundView(request, summonername)

    summonerdetail['summonerentries'] = await FetchSummonerLeagueEntry(summonerdetail['summoner'].summonerId, server)
    return summonerView(request, summonername, summonerdetail, server)

async def summonerMatchHistory(request, summonername, server):
    matchhistory = {}
    summoner = await FetchSummoner(summonername, server)
    matchhistoryFetch = await FetchSummonerMatchHistory(summoner.puuid, server)
    matchhistory['matches'] = []
    matchhistory['matches'].append(matchhistoryFetch)
    #matchhistory['summonername']
    return matchHistoryView(request, summonername, matchhistory, summoner.puuid)


async def MatchDetail(request, matchid, server):
    match = await FetchMatch(matchid, server)
    if match:
        return matchDetailView(request, match, server)
    return matchNotFoundView(request, id)
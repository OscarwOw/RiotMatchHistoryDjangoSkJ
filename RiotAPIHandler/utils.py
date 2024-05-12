# RiotAPIHandler/utils.py

from pulsefire.clients import RiotAPIClient
from Common.models import SummonerDTO, AccountDTO, LeagueEntryDTO, MatchDTO, MetadataDTO
from Common.ModelBuilder import ModelBuilder
from django.conf import settings

import asyncio


SERVER_REGION_MAP = {
        'eune': ('Europe', 'EUN1'),
        'euw': ('Europe', 'EUW1'),
        'na': ('Americas', 'NA1'),
        'kr': ('Asia', 'KR'),
        'lan': ('Americas', 'LA1'),
        'las': ('Americas', 'LA2'),
        'br': ('Americas', 'BR1'),
        'tr': ('Europe', 'TR1'),
        'ru': ('Europe', 'RU'),
        'jp': ('Asia', 'JP1'),
        'oce': ('Americas', 'OC1')
    }

async def FetchSummoner(summoner_name, server):
    print(summoner_name)
    deftagline = server
    if server=='kr':
        deftagline = 'KR1'
    if '-' in summoner_name:
        parts = summoner_name.rsplit('-', 1)
        game_name = parts[0]
        tag_line = parts[1]
    else:
        game_name = summoner_name
        tag_line = deftagline


    api_region, routing_region = SERVER_REGION_MAP.get(server, ('Europe', 'EUN1'))

    try:
        async with RiotAPIClient(default_headers={"X-Riot-Token": settings.API_KEY}) as client:
            try:
                accountdata = await client.get_account_v1_by_riot_id(region=api_region, game_name=game_name, tag_line=tag_line)
            except Exception as e:
                if e.status == 404:
                    accountdata = await client.get_account_v1_by_riot_id(region=api_region, game_name=summoner_name, tag_line=deftagline)
                else:
                    raise

            data = await client.get_lol_summoner_v4_by_puuid(region=routing_region, puuid=accountdata["puuid"])

            if data:
                account = ModelBuilder.BuildAccount(accountdata)
                summoner = ModelBuilder.BuildSummoner(data, account)
                return summoner
            else:
                return None
    except Exception as e:
        print(f"An error occurred in FetchSummoner: {e}")
        return None

async def FetchAccountByPuuid(puuid):
    try:
        async with RiotAPIClient(default_headers={"X-Riot-Token": settings.API_KEY}) as client:
            data = await client.get_account_v1_by_puuid(region="Europe", puuid=puuid)
            if data:
                acc = AccountDTO.MapToModel(data)
                return acc
            else:
                return None
    except Exception as e:
        print(f"An error occurred in FetchAccountByPuuid: {e}")
        return None



async def FetchSummonerLeagueEntry(summonerid, server):
    api_region, routing_region = SERVER_REGION_MAP.get(server, ('Europe', 'EUN1'))


    try:
        async with RiotAPIClient(
            default_headers={"X-Riot-Token": settings.API_KEY}) as client:
            data = await client.get_lol_league_v4_entries_by_summoner(region=routing_region, summoner_id=summonerid)
            if data:
                newentries = ModelBuilder.BuildEntriesDict(data)
                return newentries
            else:
                return None
    except Exception as e:
        print(f"An error occurred in FetchSummonerLeagueEntry: {e}")
        return None

async def FetchSummonerMatchHistory(puuid, server="eune"):
    api_region, routing_region = SERVER_REGION_MAP.get(server, ('Europe', 'EUN1'))
    try:
        async with (RiotAPIClient(
                default_headers={"X-Riot-Token": settings.API_KEY}) as client):

            data = await client.get_lol_match_v5_match_ids_by_puuid(region=api_region, puuid=puuid)
            firstmatches = data[:20]
            tasks = [FetchMatch(match_id, server) for match_id in firstmatches]
            matches = await asyncio.gather(*tasks)

            #match = await FetchMatch(data[0])
            if matches:
                return matches

            else:
                return None
    except Exception as e:
        print(f"An error occurred in FetchSummonerMatchHistory: {e}")
        return None

async def FetchMatch(id, server = "eune"):
    api_region, routing_region = SERVER_REGION_MAP.get(server, ('Europe', 'EUN1'))
    try:
        async with (RiotAPIClient(
            default_headers={"X-Riot-Token": settings.API_KEY}) as client):
            data = await client.get_lol_match_v5_match(region=api_region, id=id)
            participants = data['metadata']['participants']
            #resultdata = await fetch_summoner_details(participants)
            participantsdtos = data['info']['participants']
            #print(f"match: {id}")
            #for part in participantsdtos:
                #print(f"player {part['summonerName']}")

            #metadata = ModelBuilder.BuildMetadata(ModelBuilder, data['metadata'])
            #metadata = MetadataDTO.MapToModel(data['metadata'])
            #metadata.AddListOfParticipants(participants)
            #info = ModelBuilder.BuildMatchInfo(ModelBuilder, data['info'])
            #print(f"match info {info}")

            match = ModelBuilder.BuildMatch(data)
            if data:
                return match
            else:
                return None
    except Exception as e:
        print(f"An error occurred in FetchMatch: {e}")
        return None




#deprecated
async def fetch_summoner_details(participant_puuids):
    tasks = []
    for puuid in participant_puuids:
        summoner_task = FetchSummonerByPuuid(puuid)
        account_task = FetchAccountByPuuid(puuid)
        tasks.append(asyncio.gather(summoner_task, account_task))

    results = await asyncio.gather(*tasks)
    participant_objects = []
    for result in results:
        summoner, account = result
        summoner.SetAccount(account)
        participant_objects.append(summoner)

    return participant_objects

#deprecated
async def FetchSummonerByPuuid(puuid):
    #api_key = settings.RIOT_API_KEY  # Store your API key in settings.py for security
    try:
        async with RiotAPIClient(default_headers={"X-Riot-Token": settings.API_KEY}) as client:
            data = await client.get_lol_summoner_v4_by_puuid(region="EUN1", puuid=puuid)
            if data:
                summoner = ModelBuilder.BuildSummoner(data)
                #summoner = SummonerDTO.MapToModel(data)
                return summoner
            else:
                return None
    except Exception as e:
        print(f"An error occurred in FetchSummonerByPuuid: {e}")
        return None



def parseSoloQEntry(data):
    for entry in data:
        if (entry['queueType'] == 'RANKED_SOLO_5x5'):
            return entry
    return None

def parseFlexQEntry(data):
    for entry in data:
        if (entry['queueType'] == 'RANKED_FLEX_SR'):
            return entry
    return None


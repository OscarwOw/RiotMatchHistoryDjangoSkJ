# RiotAPIHandler/utils.py

from pulsefire.clients import RiotAPIClient
from Common.models import SummonerDTO, AccountDTO, LeagueEntryDTO
import asyncio

async def FetchSummoner(summoner_name):
    #api_key = settings.RIOT_API_KEY  # Store your API key in settings.py for security
    try:
        async with RiotAPIClient(default_headers={"X-Riot-Token": 'RGAPI-52d96824-f97f-428d-93ba-4f806ed7aab8'}) as client:
            account = await client.get_account_v1_by_riot_id(region="Europe", game_name=summoner_name, tag_line="EUNE")
            data = await client.get_lol_summoner_v4_by_puuid(region="EUN1", puuid=account["puuid"])
            if data:
                summoner = SummonerDTO.MapToModel(data)
                return summoner
            else:
                return None
    except Exception as e:
        print(f"An error occurred in FetchSummoner: {e}")
        return None

async def FetchAccountByPuuid(puuid):
    try:
        async with RiotAPIClient(default_headers={"X-Riot-Token": 'RGAPI-52d96824-f97f-428d-93ba-4f806ed7aab8'}) as client:
            data = await client.get_account_v1_by_puuid(region="Europe", puuid=puuid)
            if data:
                acc = AccountDTO.MapToModel(data)
                return acc
            else:
                return None
    except Exception as e:
        print(f"An error occurred in FetchAccountByPuuid: {e}")
        return None

async def FetchSummonerByPuuid(puuid):
    #api_key = settings.RIOT_API_KEY  # Store your API key in settings.py for security
    try:
        async with RiotAPIClient(default_headers={"X-Riot-Token": 'RGAPI-52d96824-f97f-428d-93ba-4f806ed7aab8'}) as client:
            data = await client.get_lol_summoner_v4_by_puuid(region="EUN1", puuid=puuid)
            if data:
                summoner = SummonerDTO.MapToModel(data)
                return summoner
            else:
                return None
    except Exception as e:
        print(f"An error occurred in FetchSummonerByPuuid: {e}")
        return None

async def FetchSummonerLeagueEntry(summonerid):
    try:
        async with RiotAPIClient(
            default_headers={"X-Riot-Token": 'RGAPI-52d96824-f97f-428d-93ba-4f806ed7aab8'}) as client:
            data = await client.get_lol_league_v4_entries_by_summoner(region="EUN1", summoner_id=summonerid)
            if data:
                entriesDict = {}
                entriesDict['soloQ'] = LeagueEntryDTO.MapToModel(parseSoloQEntry(data))
                entriesDict['flexQ'] = LeagueEntryDTO.MapToModel(parseFlexQEntry(data))
                return entriesDict
            else:
                return None
    except Exception as e:
        print(f"An error occurred in FetchSummonerLeagueEntry: {e}")
        return None

async def FetchSummonerMatchHistory(puuid):
    try:
        async with (RiotAPIClient(
                default_headers={"X-Riot-Token": 'RGAPI-52d96824-f97f-428d-93ba-4f806ed7aab8'}) as client):
            data = await client.get_lol_match_v5_match_ids_by_puuid(region="europe", puuid=puuid)
            match = await FetchMatch(data[0])

            if match:
                return match

            else:
                return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

async def FetchMatch(id):
    try:
        async with (RiotAPIClient(
            default_headers={"X-Riot-Token": 'RGAPI-52d96824-f97f-428d-93ba-4f806ed7aab8'}) as client):
            data = await client.get_lol_match_v5_match(region="europe", id=id)
            participants = data['metadata']['participants']
            resultdata = await fetch_summoner_details(participants)

            for i in resultdata:
                print(i)


            if data:
                entriesDict = {}

            else:
                return None
    except Exception as e:
        print(f"An error occurred in FetchMatch: {e}")
        return None





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


def parseSoloQEntry(data):
    for entry in data:
        if (entry['queueType'] == 'RANKED_SOLO_5x5'):
            return entry
    return None

def parseFlexQEntry(data):
    for entry in data:
        if (entry['queueType']  == 'RANKED_FLEX_SR'):
            return entry
    return None
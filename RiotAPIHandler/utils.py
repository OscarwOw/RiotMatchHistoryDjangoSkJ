# RiotAPIHandler/utils.py

from pulsefire.clients import RiotAPIClient
import requests
from django.conf import settings
from Common.models import SummonerDTO

def FetchSummoner(summoner_name):
    #api_key = settings.RIOT_API_KEY  # Store your API key in settings.py for security
    pulsefiretest("W1S OscarwOw")


    api_key = 'RGAPI-dd22f0ba-a678-476f-80e6-5cadb2309a10'  # Store your API key in settings.py for security
    url = f'https://eun1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key={api_key}'


    response = requests.get(url)
    print(response)
    if response.status_code == 200:
        summoner_data = response.json()
        # Create a new SummonerDTO object
        summoner = SummonerDTO.objects.create(
            accountId=summoner_data['accountId'],
            profileIconId=summoner_data['profileIconId'],
            revisionDate=summoner_data['revisionDate'],
            summonerId=summoner_data['id'],
            puuid=summoner_data['puuid'],
            summonerLevel=summoner_data['summonerLevel']
        )
        return summoner
    else:
        return None


async def pulsefiretest(summonername):
    async with RiotAPIClient(default_headers={"X-Riot-Token": 'RGAPI-dd22f0ba-a678-476f-80e6-5cadb2309a10'}) as client:
        account = await client.get_account_v1_by_riot_id(region="Europe", game_name=summonername, tag_line="EUNE")
        summoner = await client.get_lol_summoner_v4_by_puuid(region="Europe", puuid=account["puuid"])
        assert summoner["name"] == "W1S OscarwOw"
        assert summoner["summonerLevel"] > 200
        print('ok worked')



"""
    try:
        summoner = SummonerDTO.objects.get(name=summoner_name)
        return summoner
    except SummonerDTO.DoesNotExist:
        # If not found, fetch from Riot's API
        api_key = settings.RIOT_API_KEY  # Store your API key in settings.py for security
        url = f'https://eun1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key={api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            summoner_data = response.json()
            # Create a new SummonerDTO object
            summoner = SummonerDTO.objects.create(
                accountId=summoner_data['accountId'],
                profileIconId=summoner_data['profileIconId'],
                revisionDate=summoner_data['revisionDate'],
                summonerId=summoner_data['id'],
                puuid=summoner_data['puuid'],
                summonerLevel=summoner_data['summonerLevel']
            )
            return summoner
        else:
            return None  # Or handle errors as needed#
"""

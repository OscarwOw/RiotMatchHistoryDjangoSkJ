from django.db import models
from .MetadataDTO import MetadataDTO

class ParticipantDTO(models.Model):
    assists = models.IntegerField()
    baronKills = models.IntegerField()
    bountyLevel = models.IntegerField()
    champExperience = models.IntegerField()
    champLevel = models.IntegerField()
    championId = models.IntegerField()
    championName = models.CharField(max_length=200)
    championTransform = models.IntegerField()
    consumablesPurchased = models.IntegerField()
    damageDealtToBuildings = models.IntegerField()
    damageDealtToObjectives = models.IntegerField()
    damageDealtToTurrets = models.IntegerField()
    damageSelfMitigated = models.IntegerField()
    deaths = models.IntegerField()
    detectorWardsPlaced = models.IntegerField()
    doubleKills = models.IntegerField()
    dragonKills = models.IntegerField()
    firstBloodAssist = models.BooleanField()
    firstBloodKill = models.BooleanField()
    firstTowerAssist = models.BooleanField()
    firstTowerKill = models.BooleanField()
    gameEndedInEarlySurrender = models.BooleanField()
    gameEndedInSurrender = models.BooleanField()
    goldEarned = models.IntegerField()
    goldSpent = models.IntegerField()
    individualPosition = models.CharField(max_length=200)
    inhibitorKills = models.IntegerField()
    inhibitorTakedowns = models.IntegerField()
    inhibitorsLost = models.IntegerField()
    item0 = models.IntegerField()
    item1 = models.IntegerField()
    item2 = models.IntegerField()
    item3 = models.IntegerField()
    item4 = models.IntegerField()
    item5 = models.IntegerField()
    item6 = models.IntegerField()
    itemsPurchased = models.IntegerField()
    killingSprees = models.IntegerField()
    kills = models.IntegerField()
    lane = models.CharField(max_length=200)
    largestCriticalStrike = models.IntegerField()
    largestKillingSpree = models.IntegerField()
    largestMultiKill = models.IntegerField()
    longestTimeSpentLiving = models.IntegerField()
    magicDamageDealt = models.IntegerField()
    magicDamageDealtToChampions = models.IntegerField()
    magicDamageTaken = models.IntegerField()
    neutralMinionsKilled = models.IntegerField()
    nexusKills = models.IntegerField()
    nexusTakedowns = models.IntegerField()
    nexusLost = models.IntegerField()
    objectivesStolen = models.IntegerField()
    objectivesStolenAssists = models.IntegerField()
    participantId = models.IntegerField()
    pentaKills = models.IntegerField()
    perks = models.CharField(max_length=200) #TODO perks
    physicalDamageDealt = models.IntegerField()
    physicalDamageDealtToChampions = models.IntegerField()
    physicalDamageTaken = models.IntegerField()
    playerAugment1 = models.IntegerField()
    playerAugment2 = models.IntegerField()
    playerAugment3 = models.IntegerField()
    playerAugment4 = models.IntegerField()
    playerSubteamId = models.IntegerField()
    profileIcon = models.IntegerField()
    puuid = models.CharField(max_length=200)
    quadraKills = models.IntegerField()
    riotIdName = models.CharField(max_length=200)
    riotIdTagline = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    sightWardsBoughtInGame = models.IntegerField()
    spell1Casts = models.IntegerField()
    spell2Casts = models.IntegerField()
    spell3Casts = models.IntegerField()
    spell4Casts = models.IntegerField()
    summoner1Casts = models.IntegerField()
    summoner1Id = models.IntegerField()
    summoner2Casts = models.IntegerField()
    summoner2Id = models.IntegerField()
    summonerId = models.CharField(max_length=200)
    summonerLevel = models.IntegerField()
    summonerName = models.CharField(max_length=200)
    teamEarlySurrendered = models.BooleanField()
    teamId = models.IntegerField()
    teamPosition = models.CharField(max_length=200)
    timeCCingOthers = models.IntegerField()
    timePlayed = models.IntegerField()
    totalDamageDealt = models.IntegerField()
    totalDamageDealtToChampions = models.IntegerField()
    totalDamageShieldedOnTeammates = models.IntegerField()
    totalDamageTaken = models.IntegerField()
    totalHeal = models.IntegerField()
    totalHealsOnTeammates = models.IntegerField()
    totalMinionsKilled = models.IntegerField()
    totalTimeCCDealt = models.IntegerField()
    totalTimeSpentDead = models.IntegerField()
    totalUnitsHealed = models.IntegerField()
    tripleKills = models.IntegerField()
    trueDamageDealt = models.IntegerField()
    trueDamageDealtToChampions = models.IntegerField()
    trueDamageTaken = models.IntegerField()
    turretKills = models.IntegerField()
    turretTakedowns = models.IntegerField()
    turretsLost = models.IntegerField()
    unrealKills = models.IntegerField()
    visionScore = models.IntegerField()
    visionWardsBoughtInGame = models.IntegerField()
    wardsKilled = models.IntegerField()
    wardsPlaced = models.IntegerField()
    win = models.BooleanField()

    def __str__(self):
        return (f"summonerName: {self.summonerName}")

    def __getitem__(self, key):
        return getattr(self, key, None)

    @classmethod
    def MapToModel(cls, data):
        return cls(
            assists=data.get('assists', 0),
            baronKills=data.get('baronKills', 0),
            bountyLevel=data.get('bountyLevel', 0),
            champExperience=data.get('champExperience', 0),
            champLevel=data.get('champLevel', 0),
            championId=data.get('championId', 0),
            championName=data.get('championName', ''),
            championTransform=data.get('championTransform', 0),
            consumablesPurchased=data.get('consumablesPurchased', 0),
            damageDealtToBuildings=data.get('damageDealtToBuildings', 0),
            damageDealtToObjectives=data.get('damageDealtToObjectives', 0),
            damageDealtToTurrets=data.get('damageDealtToTurrets', 0),
            damageSelfMitigated=data.get('damageSelfMitigated', 0),
            deaths=data.get('deaths', 0),
            detectorWardsPlaced=data.get('detectorWardsPlaced', 0),
            doubleKills=data.get('doubleKills', 0),
            dragonKills=data.get('dragonKills', 0),
            firstBloodAssist=data.get('firstBloodAssist', False),
            firstBloodKill=data.get('firstBloodKill', False),
            firstTowerAssist=data.get('firstTowerAssist', False),
            firstTowerKill=data.get('firstTowerKill', False),
            gameEndedInEarlySurrender=data.get('gameEndedInEarlySurrender', False),
            gameEndedInSurrender=data.get('gameEndedInSurrender', False),
            goldEarned=data.get('goldEarned', 0),
            goldSpent=data.get('goldSpent', 0),
            individualPosition=data.get('individualPosition', ''),
            inhibitorKills=data.get('inhibitorKills', 0),
            inhibitorTakedowns=data.get('inhibitorTakedowns', 0),
            inhibitorsLost=data.get('inhibitorsLost', 0),
            item0=data.get('item0', 0),
            item1=data.get('item1', 0),
            item2=data.get('item2', 0),
            item3=data.get('item3', 0),
            item4=data.get('item4', 0),
            item5=data.get('item5', 0),
            item6=data.get('item6', 0),
            itemsPurchased=data.get('itemsPurchased', 0),
            killingSprees=data.get('killingSprees', 0),
            kills=data.get('kills', 0),
            lane=data.get('lane', ''),
            largestCriticalStrike=data.get('largestCriticalStrike', 0),
            largestKillingSpree=data.get('largestKillingSpree', 0),
            largestMultiKill=data.get('largestMultiKill', 0),
            longestTimeSpentLiving=data.get('longestTimeSpentLiving', 0),
            magicDamageDealt=data.get('magicDamageDealt', 0),
            magicDamageDealtToChampions=data.get('magicDamageDealtToChampions', 0),
            magicDamageTaken=data.get('magicDamageTaken', 0),
            neutralMinionsKilled=data.get('neutralMinionsKilled', 0),
            nexusKills=data.get('nexusKills', 0),
            nexusTakedowns=data.get('nexusTakedowns', 0),
            nexusLost=data.get('nexusLost', 0),
            objectivesStolen=data.get('objectivesStolen', 0),
            objectivesStolenAssists=data.get('objectivesStolenAssists', 0),
            participantId=data.get('participantId', 0),
            pentaKills=data.get('pentaKills', 0),
            physicalDamageDealt=data.get('physicalDamageDealt', 0),
            physicalDamageDealtToChampions=data.get('physicalDamageDealtToChampions', 0),
            physicalDamageTaken=data.get('physicalDamageTaken', 0),
            playerAugment1=data.get('playerAugment1', 0),
            playerAugment2=data.get('playerAugment2', 0),
            playerAugment3=data.get('playerAugment3', 0),
            playerAugment4=data.get('playerAugment4', 0),
            playerSubteamId=data.get('playerSubteamId', 0),
            profileIcon=data.get('profileIcon', 0),
            puuid=data.get('puuid', ''),
            quadraKills=data.get('quadraKills', 0),
            riotIdName=data.get('riotIdName', ''),
            riotIdTagline=data.get('riotIdTagline', ''),
            role=data.get('role', ''),
            sightWardsBoughtInGame=data.get('sightWardsBoughtInGame', 0),
            spell1Casts=data.get('spell1Casts', 0),
            spell2Casts=data.get('spell2Casts', 0),
            spell3Casts=data.get('spell3Casts', 0),
            spell4Casts=data.get('spell4Casts', 0),
            summoner1Casts=data.get('summoner1Casts', 0),
            summoner1Id=data.get('summoner1Id', 0),
            summoner2Casts=data.get('summoner2Casts', 0),
            summoner2Id=data.get('summoner2Id', 0),
            summonerId=data.get('summonerId', ''),
            summonerLevel=data.get('summonerLevel', 0),
            summonerName=data.get('summonerName', ''),
            teamEarlySurrendered=data.get('teamEarlySurrendered', False),
            teamId=data.get('teamId', 0),
            teamPosition=data.get('teamPosition', ''),
            timeCCingOthers=data.get('timeCCingOthers', 0),
            timePlayed=data.get('timePlayed', 0),
            totalDamageDealt=data.get('totalDamageDealt', 0),
            totalDamageDealtToChampions=data.get('totalDamageDealtToChampions', 0),
            totalDamageShieldedOnTeammates=data.get('totalDamageShieldedOnTeammates', 0),
            totalDamageTaken=data.get('totalDamageTaken', 0),
            totalHeal=data.get('totalHeal', 0),
            totalHealsOnTeammates=data.get('totalHealsOnTeammates', 0),
            totalMinionsKilled=data.get('totalMinionsKilled', 0),
            totalTimeCCDealt=data.get('totalTimeCCDealt', 0),
            totalTimeSpentDead=data.get('totalTimeSpentDead', 0),
            totalUnitsHealed=data.get('totalUnitsHealed', 0),
            tripleKills=data.get('tripleKills', 0),
            trueDamageDealt=data.get('trueDamageDealt', 0),
            trueDamageDealtToChampions=data.get('trueDamageDealtToChampions', 0),
            trueDamageTaken=data.get('trueDamageTaken', 0),
            turretKills=data.get('turretKills', 0),
            turretTakedowns=data.get('turretTakedowns', 0),
            turretsLost=data.get('turretsLost', 0),
            unrealKills=data.get('unrealKills', 0),
            visionScore=data.get('visionScore', 0),
            visionWardsBoughtInGame=data.get('visionWardsBoughtInGame', 0),
            wardsKilled=data.get('wardsKilled', 0),
            wardsPlaced=data.get('wardsPlaced', 0),
            win=data.get('win', False)
        )


    def save(self, *args, **kwargs):
        pass
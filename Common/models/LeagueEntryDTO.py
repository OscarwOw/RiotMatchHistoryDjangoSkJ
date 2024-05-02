from django.db import models
from .MiniSeriesDTO import MiniSeriesDTO

class LeagueEntryDTO(models.Model):
    leagueId = models.CharField(max_length=200)
    summonerId = models.CharField(max_length=200)
    queueType = models.CharField(max_length=200)
    tier = models.CharField(max_length=200)
    rank = models.CharField(max_length=200)
    leaguePoints = models.BigIntegerField()
    wins = models.BigIntegerField()
    losses = models.BigIntegerField()
    hotStreak = models.BooleanField()
    veteran = models.BooleanField()
    freshBlood = models.BooleanField()
    inactive = models.BooleanField()
    miniSeries = models.OneToOneField(MiniSeriesDTO, on_delete=models.CASCADE, null=True,
                                      blank=True)

    def __str__(self):
        return (f"leagueId: {self.leagueId}, summonerId: {self.summonerId}, queueType: {self.queueType}, "
                f"tier: {self.tier}, rank: {self.rank}, leaguePoints: {self.leaguePoints}, "
                f"wins: {self.wins}, losses: {self.losses}, hotStreak: {self.hotStreak}, "
                f"veteran: {self.veteran}, freshBlood: {self.freshBlood}, inactive: {self.inactive}, ")

    @classmethod
    def MapToModel(cls, data):
        return cls(
            leagueId=data.get('leagueId', ''),
            queueType=data.get('queueType', ''),
            tier=data.get('tier', ''),
            rank=data.get('rank', ''),
            summonerId=data.get('summonerId', ''),
            leaguePoints=data.get('leaguePoints', 0),
            wins=data.get('wins', 0),
            losses=data.get('losses', 0),
            veteran=data.get('veteran', False),
            inactive=data.get('inactive', False),
            freshBlood=data.get('freshBlood', False),
            hotStreak=data.get('hotStreak', False)
        )
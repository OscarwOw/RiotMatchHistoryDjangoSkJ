from django.db import models

class SummonerDTO(models.Model):
    accountId = models.CharField(max_length=56, unique=True)
    profileIconId = models.IntegerField()
    revisionDate = models.BigIntegerField()
    summonerId = models.CharField(max_length=63, unique=True)
    puuid = models.CharField(max_length=78, unique=True)
    summonerLevel = models.BigIntegerField()

    def __str__(self):
        return self.summonerId



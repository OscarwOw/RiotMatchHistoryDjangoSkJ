from django.db import models
from .AccountDTO import AccountDTO

class SummonerDTO(models.Model):
    accountId = models.CharField(max_length=200)
    profileIconId = models.IntegerField()
    revisionDate = models.BigIntegerField()
    summonerId = models.CharField(max_length=200)
    puuid = models.CharField(max_length=200)
    summonerLevel = models.BigIntegerField()
    Account = models.OneToOneField(AccountDTO, on_delete=models.CASCADE, null=True,
                                      blank=True)

    def __str__(self):
        if self.Account:
            acc = self.Account
        else:
            acc = ''
        return (f"accountId: {self.accountId}, profileIconId: {self.profileIconId}, revisionDate: {self.revisionDate}, "
                f"summonerId: {self.summonerId}, puuid: {self.puuid}, summonerLevel: {self.summonerLevel}, "
                f"Account: {acc}")

    @classmethod
    def MapToModel(cls, data):
        return cls(
            accountId=data.get('accountId', ''),
            profileIconId=data.get('profileIconId', 0),
            revisionDate=data.get('revisionDate', 0),
            summonerId=data.get('id', ''),
            puuid=data.get('puuid', ''),
            summonerLevel=data.get('summonerLevel', 0)
        )

    def SetAccount(self, account):
        self.Account = account


from django.db import models

class AccountDTO(models.Model):
    puuid = models.CharField(max_length=200)
    gameName = models.CharField(max_length=200)
    tagLine = models.CharField(max_length=200)

    def __str__(self):
        return (f"puuid: {self.puuid}, gameName: {self.gameName}, tagLine: {self.tagLine}" )

    def __getitem__(self, key):
        return getattr(self, key, None)

    @classmethod
    def MapToModel(cls, data):
        return cls(
            puuid=data.get('puuid', ''),
            gameName=data.get('gameName', ''),
            tagLine=data.get('tagLine', '')
        )


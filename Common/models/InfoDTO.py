from django.db import models

class InfoDTO(models.Model):
    endOfGameResult = models.CharField(max_length=200)
    gameCreation = models.BigIntegerField()
    gameDuration = models.BigIntegerField()
    gameEndTimestamp = models.BigIntegerField()
    gameId = models.BigIntegerField()
    gameMode = models.CharField(max_length=200)
    gameName = models.CharField(max_length=200)
    gameStartTimestamp = models.BigIntegerField()
    gameType = models.CharField(max_length=200)
    gameVersion = models.CharField(max_length=200)
    mapId = models.IntegerField()
    participants = models.JSONField(default=list)
    platformId = models.CharField(max_length=200)
    queueId = models.IntegerField()
    teams = models.JSONField(default=list)
    tournamentCode = models.CharField(max_length=200)


    def save(self, *args, **kwargs):
        pass

    def __str__(self):
        return (f"gameDuration: {self.gameDuration}, gameCreation: {self.gameCreation}, \nfirstparticipant: {self.participants[0]},  ")

    def __getitem__(self, key):
        return getattr(self, key, None)

    @classmethod
    def MapToModel(cls, data):
        instance = cls(
            endOfGameResult=data.get('endOfGameResult', ''),
            gameCreation=data.get('gameCreation', 0),
            gameDuration=data.get('gameDuration', 0),
            gameEndTimestamp=data.get('gameEndTimestamp', 0),
            gameId=data.get('gameId', 0),
            gameMode=data.get('gameMode', ''),
            gameName=data.get('gameName', ''),
            gameStartTimestamp=data.get('gameStartTimestamp', 0),
            gameType=data.get('gameType', ''),
            gameVersion=data.get('gameVersion', ''),
            mapId=data.get('mapId', 0),
            platformId=data.get('platformId', ''),
            queueId=data.get('queueId', 0),
            tournamentCode=data.get('tournamentCode', '')
        )
        return instance

    def AddListOfParticipants(self, list):
        self.participants.extend(list)

    def AddListOfTeams(self, list):
        self.teams.extend(list)

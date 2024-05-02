from django.db import models

class MetadataDTO(models.Model):
    dataVersion = models.CharField(max_length=200)
    matchId = models.CharField(max_length=200)
    participants = models.ManyToManyField('SummonerDTO', related_name='matches')

#summoners = metadata.participants.all() access from metadata
#matches = summoner1.matches.all() access from summoner


#structure how to add and access participants
#metadata = MetadataDTO.objects.create(dataVersion='1.0', matchId='12345')
#summoner1 = SummonerDTO.objects.create(summonerName='Summoner1')
#summoner2 = SummonerDTO.objects.create(summonerName='Summoner2')
#metadata.participants.add(summoner1, summoner2)


    def __str__(self):
        participant_details = ', '.join([str(participant) for participant in self.participants.all()])
        return (f"dataVersion: {self.dataVersion}, matchId: {self.matchId}, participants: {participant_details}, ")

    @classmethod
    def MapToModel(cls, data):
        return cls(
            dataVersion=data.get('dataVersion', ''),
            matchId=data.get('matchId', '')
        )

    def AddListOfParticipants(self, list):
        for participant in list:
            self.participants.add(participant)

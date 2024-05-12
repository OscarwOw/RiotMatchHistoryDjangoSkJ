from django.db import models

class MetadataDTO(models.Model):
    dataVersion = models.CharField(max_length=200)
    matchId = models.CharField(max_length=200)
    #participants = models.ManyToManyField('SummonerDTO', related_name='matches')
    participants = []
#summoners = metadata.participants.all() access from metadata
#matches = summoner1.matches.all() access from summoner


#structure how to add and access participants
#metadata = MetadataDTO.objects.create(dataVersion='1.0', matchId='12345')
#summoner1 = SummonerDTO.objects.create(summonerName='Summoner1')
#summoner2 = SummonerDTO.objects.create(summonerName='Summoner2')
#metadata.participants.add(summoner1, summoner2)

    def save(self, *args, **kwargs):
        # Override the save method to do nothing
        pass

    def __str__(self):
        participant_details = ',\n '.join([str(participant) for participant in self.participants])
        return (f"dataVersion: {self.dataVersion}, matchId: {self.matchId}, participants: {participant_details}, ")

    def __getitem__(self, key):
        return getattr(self, key, None)

    @classmethod
    def MapToModel(cls, data):
        instance = cls(
            dataVersion=data.get('dataVersion', ''),
            matchId=data.get('matchId', '')
        )
        # Normally we would call save() here, but it's overridden to do nothing
        return instance

    def AddListOfParticipants(self, list):
        self.participants.extend(list)

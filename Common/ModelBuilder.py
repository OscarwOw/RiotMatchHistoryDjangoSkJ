from .models.SummonerDTO import SummonerDTO
from .models.AccountDTO import AccountDTO
from .models.LeagueEntryDTO import LeagueEntryDTO
from .models.MetadataDTO import MetadataDTO
from .models.MatchDTO import MatchDTO
from .models.InfoDTO import InfoDTO
from .models.ParticipantDTO import ParticipantDTO

class ModelBuilder:
    @staticmethod
    def BuildSummoner(summonerdata, Account=None):

        summoner = SummonerDTO.MapToModel(summonerdata)
        if(Account != None):
            summoner.SetAccount(Account)
        return summoner

    @staticmethod
    def BuildAccount(account):
        return AccountDTO.MapToModel(account)

    @staticmethod
    def BuildEntriesDict( data):
        entries = {}
        soloEntry = ModelBuilder.parseSoloQEntry(data)
        flexEntry = ModelBuilder.parseFlexQEntry(data)
        if(soloEntry):
            soloEntryModel = LeagueEntryDTO.MapToModel(soloEntry)
            entries['soloQ'] = soloEntryModel
        if(flexEntry):
            flexEntryModel = LeagueEntryDTO.MapToModel(flexEntry)
            entries['flexQ'] = flexEntryModel
        return entries

    @staticmethod
    def BuildMatch(input):
        match = MatchDTO()
        info = ModelBuilder.BuildMatchInfo(input['info'])
        metadata = ModelBuilder.BuildMetadata(input['metadata'])
        match.SetInfo(info)
        match.SetMetadata(metadata)
        return match

    @staticmethod
    def BuildMetadata(data):
        metadata = MetadataDTO.MapToModel(data)
        metadata.AddListOfParticipants(data['participants'])
        return metadata

    @staticmethod
    def BuildMatchInfo(data):
        infodata = InfoDTO.MapToModel(data)
        participants = []
        for participant in data['participants']:
            newparticipant = ModelBuilder.BuildParticipant(participant)
            participants.append(newparticipant)
        infodata.AddListOfParticipants(participants)
        return infodata

    @staticmethod
    def BuildParticipant(data):
        participant = ParticipantDTO.MapToModel(data)
        return participant




#helperfunctions
    def parseSoloQEntry(data):
        for entry in data:
            if (entry['queueType'] == 'RANKED_SOLO_5x5'):
                return entry
        return None

    def parseFlexQEntry(data):
        for entry in data:
            if (entry['queueType'] == 'RANKED_FLEX_SR'):
                return entry
        return None

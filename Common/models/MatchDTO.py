from django.db import models
from MetadataDTO import MetadataDTO

class MatchDTO(models.Model):
    metadata = models.OneToOneField(MetadataDTO)
    #info = models.OneToOneField(InfoDTO) TODO info

    def __str__(self):
        return (f"metadata: {self.metadata}")

    def SetMetadata(self, metadata):
        self.metadata = metadata

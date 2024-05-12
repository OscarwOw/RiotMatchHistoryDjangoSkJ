from django.db import models
from .MetadataDTO import MetadataDTO
from .InfoDTO import InfoDTO

class MatchDTO(models.Model):
    metadata = models.OneToOneField(MetadataDTO, on_delete=models.CASCADE, null=True,
                                      blank=True)
    info = models.OneToOneField(InfoDTO, on_delete=models.CASCADE, null=True,
                                      blank=True)

    def __str__(self):
        return (f"metadata: {self.metadata}")

    def __getitem__(self, key):
        return getattr(self, key, None)

    def SetMetadata(self, metadata):
        self.metadata = metadata

    def SetInfo(self, info):
        self.info = info

    def save(self, *args, **kwargs):
        pass
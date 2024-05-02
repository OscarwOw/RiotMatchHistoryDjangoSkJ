from django.db import models

class MiniSeriesDTO(models.Model):
    losses = models.BigIntegerField()
    progress = models.CharField(max_length=200)
    target = models.BigIntegerField()
    wins = models.BigIntegerField()

    def __str__(self):
        return f"losses: {self.losses}, progress: {self.progress}, target: {self.target}, wins: {self.wins}"

from django.db import models


class TreasureStatus(models.Model):
    status = models.CharField(max_length=32)

    def __str__(self):
        return self.status


class Treasure(models.Model):
    checksum = models.CharField(max_length=64)
    headline = models.CharField(max_length=512)
    content = models.TextField()
    origin = models.CharField(max_length=512)
    pub_date = models.DateTimeField('published')

    def __str__(self):
        return self.headline

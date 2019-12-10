from django.db import models
from django.contrib.postgres.fields import JSONField

class Participant(models.Model):
    parID = models.CharField(max_length = 100, primary_key=True)
    parCol = models.CharField(max_length = 100)
    parAns = models.TextField()

class CollectionAnswer(models.Model):
    colID = models.CharField(max_length = 100, primary_key=True)
    colPar = models.TextField()
    colAns = models.TextField()


class GiftParticipant(models.Model):
    parID = models.CharField(max_length = 100, primary_key=True)
    parStories = models.TextField()
    parChapters = models.TextField()
    parExhibits = models.TextField()

#giftID = models.CharField(max_length = 100, primary_key=True)
#parID = models.ForeignKey(GiftParticipant, on_delete=models.CASCADE)
class GiftAnswers(models.Model):
    modID = models.CharField(max_length = 100, blank= True)
    parID = models.CharField(max_length = 100, blank= True)
    giftWord = models.CharField(max_length = 100, blank= True)
    giftFree = models.CharField(max_length = 100, blank= True)
    giftArou = models.CharField(max_length = 100, blank= True)
    giftVael = models.CharField(max_length = 100, blank= True)

class StorageSettings(models.Model):
    userID = models.CharField(max_length = 100)
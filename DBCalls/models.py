from django.db import models

class Collection(models.Model):
    colID = models.CharField(max_length = 100, primary_key=True)
    colName = models.CharField(max_length = 100)
    colExh = models.TextField(blank = True)
    colMods = models.TextField(blank = True)

class Exhibit(models.Model):
    exhID = models.CharField(max_length = 100, primary_key=True)
    exhName = models.CharField(max_length = 100)
    exhIMG = models.TextField()
    exhDesc = models.TextField()
    exhMods = models.TextField(blank = True)

class Module(models.Model):
    modID = models.CharField(max_length = 100, primary_key=True)
    modName = models.CharField(max_length = 100)
    modType = models.CharField(max_length = 100)
    modQuestions = models.TextField()

class Question(models.Model):
    queID = models.CharField(max_length = 100, primary_key=True)
    queTitle = models.CharField(max_length = 100)
    queType = models.CharField(max_length = 100)
    queExtras = models.TextField(blank = True)
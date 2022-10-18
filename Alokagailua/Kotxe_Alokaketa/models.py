from django.db import models

# Create your models here.

class Pertsona(models.Model):
    izena = models.CharField(max_length=50)
    abizena = models.CharField(max_length=50)
    def __str__(self): # objetuari deitzerakoan self.*** jartzen dugunari deitzen diogu
        return u'%s'%self.izena

class Kotxea(models.Model):
    modeloa = models.CharField(max_length=50)
    kolorea = models.CharField(max_length=50)
    alokatzedata = models.CharField(max_length=50)
    pertsona = models.ForeignKey(Pertsona, on_delete=models.CASCADE, null=True)
    def __str__(self): # objetuari deitzerakoan self.*** jartzen dugunari deitzen diogu
        return u'%s'%self.modeloa
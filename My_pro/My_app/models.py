from django.db import models


class School(models.Model):

    name  = models.CharField(max_length = 250)
    princubel = models.CharField(max_length = 250)
    localisation = models.CharField(max_length = 250)
    #date  = models.DateField()

    def __str__(self):
        return self.name

class Etud (models.Model):

    
    name = models.CharField(max_length = 250)
    prenom = models.CharField(max_length = 250)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
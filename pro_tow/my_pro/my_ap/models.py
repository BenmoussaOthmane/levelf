from django.db import models 
from django.urls import reverse
# Create your models here.≠

class Produite (models.Model) :
    name = models.CharField(max_length = 250)
    qte = models.PositiveIntegerField()
    #date = models.DateField()

    def __str__(self):

        return self.name
        
    #  hadi bah ki ajoute wahad jdiid  yadihli la tabel lazamm ndirha fi col table baghi ajoutyer fiha

    def get_absolute_url(self):
        return reverse("my_ap:detail" , args=[str(self.pk)])


class Livrision(models.Model):
    produite = models.ForeignKey(Produite, on_delete=models.CASCADE , related_name='produite')
    fournisseur = models.CharField(max_length = 250)
    time = models.TimeField()
    prix = models.IntegerField()

    def __str__(self):
        return self.fournisseur


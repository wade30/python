from django.db import models


class Trajet(models.Model):
    depart = models.CharField(max_length=30)
    arrivee = models.CharField(max_length=30)

    def __str__(self):
        return "depart: %s <br> <br> arrivee: %s" % (self.depart, self.arrivee)


class Compagnie(models.Model):
    nom = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='media')

    def __str__(self):
        return self.nom + ' ' + self.logo


class Vol(models.Model):
    prix = models.FloatField()
    date = models.DateField()
    heure = models.TimeField()
    trajet = models.ForeignKey(Trajet, on_delete=models.CASCADE)
    compagnie = models.ManyToManyField(Compagnie, related_name='vols')

    def __str__(self):
        return str(self.prix) + ' ' + str(self.date) + ' ' + str(self.heure)+' '+str(self.trajet)+' '+str(self.compagnie)

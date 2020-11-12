from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Localisation(models.Model):
    continent = models.CharField()
    city = models.CharField()
    
    def __str__(self):
        return self.continent+"/"+self.city

class Profil(models.Model):
    user = models.OneToOneField(User)
    localisations = models.ManyToManyField(Localisation)

    def __str__(self):
        return self.user.username
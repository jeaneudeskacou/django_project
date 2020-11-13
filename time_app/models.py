from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Localisation(models.Model):
    continent = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    
    def __str__(self):
        return self.continent+"/"+self.city

class Profil(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    localisations = models.ManyToManyField(Localisation)

    def __str__(self):
        return self.user.username
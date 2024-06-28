from django.db import models

# Create your models here.

class TestModel(models.Model):
    
    title           = models.CharField(max_length=255, null=True, blank=True)
    description     = models.CharField(max_length=655, null=True, blank=True)
    
    def __str__(self):
        return self.title


# class Game(models.Model):
    
#     gamemode        = models.CharField()
#     players         = models.ManyToManyField()
    

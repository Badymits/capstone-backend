from django.db import models

from django.conf import settings

# Create your models here.
class Lobby(models.Model):
    
    owner                   = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created            = models.DateTimeField(auto_now_add=True)
    players                 = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='players')
    lobby_code              = models.CharField(unique=True, max_length=6)
    
    
    def __str__(self):
        return f'room created by {self.owner.username}'



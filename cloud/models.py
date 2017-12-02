from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='prof')
    pin  = models.CharField(max_length=10)
    token = models.CharField(null=True, blank=True, max_length=256)

class Door(models.Model):
    open = models.BooleanField(default=False)

class Log(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    usuari   = models.ForeignKey(Profile, null=True)
    portaOberta = models.NullBooleanField(null=True)
    contrasenyaValida = models.NullBooleanField(null=True)

    @property
    def get_username(self):
        if self.usuari is None:
            return None
        return self.usuari.user.username

    def __str__(self):
        if self.contrasenyaValida is None:
            if self.portaOberta:
                return "Porta oberta"
            return "Porta tancada"
        else:
            if self.contrasenyaValida:
                return self.usuari.user.username + " ha obert la porta"
            return "Pin incorrecte"
        return "Log entry"
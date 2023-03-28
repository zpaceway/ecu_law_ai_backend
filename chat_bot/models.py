from django.db import models


class Pragma(models.Model):
    name = models.CharField(max_length=128)
    file = models.FileField()

    def __str__(self) -> str:
        return self.name

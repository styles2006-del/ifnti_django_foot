from django.db import models


class Equipe(models.Model):
    nom = models.CharField(max_length=120)
    promo = models.CharField(max_length=120)

    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'equipe'
        verbose_name_plural = 'equipe'


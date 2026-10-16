from django.db import models


class Equipe(models.Model):
    nom = models.CharField(max_length=120, unique=True)
    promo = models.CharField(max_length=120)


    def __str__(self):
        return f"{self.nom}"

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'equipe'
        verbose_name_plural = 'equipes'

class Match(models.Model):

    domicile = models.ForeignKey(
        Equipe, 
        on_delete=models.CASCADE, 
        related_name='matchs_a_domicile'
    )
    
    visiteur = models.ForeignKey(
        Equipe, 
        on_delete=models.CASCADE, 
        related_name='matchs_a_l_exterieur'
    )

    date_match = models.DateTimeField(null=True, blank=True)

    score_domicile = models.IntegerField(null=True, blank=True)
    score_visiteur = models.IntegerField(null=True, blank=True)

    def __str__(self):

        if self.score_domicile is None or self.score_visiteur is None:

            return f"{self.domicile} - {self.visiteur} : à jouer"
        
        return f"{self.domicile} - {self.visiteur} : {self.score_domicile}-{self.score_visiteur}"


import pytest
from django.db import IntegrityError

from tournoi.models.equipe import Equipe

def test_une_equipe_a_un_nom_et_une_promo(db):

    equipe=Equipe.objects.create(nom='Les lions',promo='L1')

    assert equipe.nom
    assert equipe.promo

def test_une_equipe_a_un_non(db):

    equipe1=Equipe.objects.create(nom='Les lions',promo='L1')


    with pytest.raises(IntegrityError):

        equipe1=Equipe.objects.create(nom='Les lions',promo='L2')

            
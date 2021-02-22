from exercices.exercice2 import *

from math import sqrt   # import de la fonction racine carrée


def test_distance():
    assert distance((1, 0), (5, 3)) == 5.0, "erreur de calcul"

def test_plus_courte_distance():
    assert plus_courte_distance([(7, 9), (2, 5), (5, 2)], (0, 0)) == (2, 5), "erreur"

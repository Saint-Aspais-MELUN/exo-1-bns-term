from exercices.exercice1 import *
def test_recherche():
    ## Ici le code d'initialisation si nécessaire
    assert recherche([5, 3],1) == 2
    assert recherche([2,4],2) == 0
    assert recherche([2,3,5,2,4],2) == 3

#!pip install pytest

import pytest

from calcul import Calcul

# Fixture pour créer une instance de la 
# classe Calcul pour chaque test
@pytest.fixture
def calculatrice():
    return Calcul()

# Tests

# Test d'addition
def test_additionner(calculatrice):
    resultat = calculatrice.additionner(3, 5)
    assert resultat == 8

# Test de soustraction
def test_soustraire(calculatrice):
    resultat = calculatrice.soustraire(10, 4)
    assert resultat == 6

# Test de multiplication
def test_multiplier(calculatrice):
    resultat = calculatrice.multiplier(2, 3)
    assert resultat == 6

# Test de division
def test_diviser(calculatrice):
    resultat = calculatrice.diviser(8, 2)
    assert resultat == 4
    
# def test_diviser_par_zero(calculatrice):
#     with pytest.raises(ZeroDivisionError, match="Division par zéro impossible"):
#         calculatrice.diviser(6, 0)
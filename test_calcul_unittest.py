import unittest

# Importer la classe Calcul

from calcul import Calcul

# kjdhkdsjfhkds

# Classe de tests héritant de unittest.TestCase
class TestCalcul(unittest.TestCase):

    # Méthode de configuration exécutée avant chaque test
    def setUp(self):
        # Initialisation des ressources nécessaires pour les tests
        self.calc = Calcul()

    # Test d'addition
    def test_additionner(self):
        resultat = self.calc.additionner(3, 5)
        # Vérifier si le résultat est égal à 8
        self.assertEqual(resultat, 8)

    # Test soustraction
    def test_soustraire(self):
        resultat = self.calc.soustraire(10, 4)
        self.assertEqual(resultat, 6)

    # Test de multiplication
    def test_multiplier(self):
        resultat = self.calc.multiplier(3, 8)
        self.assertEqual(resultat, 24)

    #Test de division
    def test_diviser(self):
        resultat = self.calc.diviser(15, 3)
        self.assertEqual(resultat, 5)

    # Test de div by zero
    # def test_diviser_by_zero(self):
    #     resultat = self.calc.diviser(15, 0)
    #     self.assertEqual(resultat, "Division par zéro impossible")
    def test_diviser_by_zero(self):
        resultat = self.calc.diviser(15, 0)
        self.assertRaises(Exception, self.calc.diviser(15, 0))

# Exécuter les tests si le script est exécuté directement
if __name__ == '__main__':
    unittest.main()
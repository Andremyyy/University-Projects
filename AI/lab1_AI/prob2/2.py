# Să se determine distanța Euclideană
# între două locații identificate prin
# perechi de numere.
# De ex. distanța între (1,5) și (4,1) este 5.0


import math

# Complexitate timp: O(1), pt ca avem doar operatii matematice
# Complexitate spatiala: O(1), pt ca nu utilez structuri de date suplimentare

# Aceeasi solutia generata si de bot inteligent!!!

def distanta_euclidiana(x1, y1, x2, y2):
    """
        Calculează distanța euclideană dintre două puncte într-un plan 2D folosind formula matematica.

        :param x1, y1: Coordonatele primului punct.
        :param x2, y2: Coordonatele celui de-al doilea punct.
        :return: Distanța euclideană dintre cele două puncte.


        """
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def test_distanta_euclidiana():
    assert distanta_euclidiana(0, 0, 3, 4) == 5.0
    assert distanta_euclidiana(-1, -1, 2, 3) == 5.0
    assert distanta_euclidiana(0, 0, 0, 0) == 0.0
    assert distanta_euclidiana(1, 1, 1, 2) == 1.0
    assert distanta_euclidiana(2, 2, 5, 6) == 5.0
    print("Testele au trecut cu succes!")


if __name__ == '__main__':
    test_distanta_euclidiana()
    print(distanta_euclidiana(1, 5, 4, 1))
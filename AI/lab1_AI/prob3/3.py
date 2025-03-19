# Să se determine produsul scalar
# a doi vectori rari care conțin numere reale.
# Un vector este rar atunci când conține multe elemente nule.
# Vectorii pot avea oricâte dimensiuni.
# De ex. produsul scalar a 2 vectori unisimensionali
# [1,0,2,0,3] și [1,2,0,3,1] este 4.

# Complexitate timp: O(n), pt ca parcurgem toate valorile din vectori
# Complexitate spatiala: O(1), pt ca nu utilez structuri de date suplimentare

def produs_scalar (v1, v2):
    """
        Calculează produsul scalar a doi vectori rari.

        :param v1: Lista de numere reale (vector rar)
        :param v2: Lista de numere reale (vector rar)
        :return: Produsul scalar al celor doi vectori
        """
    produs = 0
    i = 0
    while (i < len(v1)):
        if v1[i] != 0 and v2[i] != 0:
            produs += v1[i] * v2[i]
        i+=1

    return produs

def test_produs_scalar():
    assert produs_scalar([0, 0, 0, 0, 0], [1, 2, 3, 4, 5]) == 0
    assert produs_scalar([1, 2, 3], [4, 5, 6]) == 1*4 + 2*5 + 3*6  # 32
    assert produs_scalar([1.5, 0, 2.5], [0, 3, 1.5]) == 2.5 * 1.5  # 3.75
    print("Testele au trecut cu succes!")

if __name__ == '__main__':
    print(produs_scalar([1,0,2,0,3], [1,2,0,3,1]))
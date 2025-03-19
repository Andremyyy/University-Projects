# Considerându-se o matrice cu n x m elemente întregi și o listă cu perechi formate
# din coordonatele a 2 căsuțe din matrice ((p,q) și (r,s)),
# să se calculeze suma elementelor din sub-matricile identificate de fieare pereche.
#
# De ex, pt matricea
# [[0, 2, 5, 4, 1],
#  [4, 8, 2, 3, 7],
#  [6, 3, 4, 6, 2],
#  [7, 3, 1, 8, 3],
#  [1, 5, 7, 9, 4]]
# și lista de perechi ((1, 1) și (3, 3)), ((2, 2) și (4, 4)),
# suma elementelor din prima sub-matrice este 38, iar suma elementelor din a 2-a sub-matrice este 44.



# Complexitate timp: O(n*m), pt ca parcurg matricea normal
# Complexitate spatiala: O(1), pt ca stochez doar intr-o variabila simpla

def suma_sub_matrice(matrice, p, q, r, s):
    """
    Calculează suma tuturor elementelor dintr-o sub-matrice a unei matrice date.

    Metodă:
        1. Se inițializează o variabilă suma cu valoarea 0.
        2. Se parcurg toate elementele din sub-matricea definită de colțurile (p, q) și (r, s).
        3. Se adaugă fiecare element la suma.

    :param matrice: listă de liste de numere întregi reprezentând matricea inițială.
    :param (p, q): coordonatele colțului stânga-sus al sub-matricei.
    :param (r, s): coordonatele colțului dreapta-jos al sub-matricei.
    :return : un număr întreg care reprezintă suma elementelor din sub-matricea selectată.
    """
    suma = 0
    for i in range(p,r+1):
        for j in range(q,s+1):
            suma += matrice[i][j]

    return suma


def test_suma_sub_matrice():
    matrice = [
        [0, 2, 5, 4, 1],
        [4, 8, 2, 3, 7],
        [6, 3, 4, 6, 2],
        [7, 3, 1, 8, 3],
        [1, 5, 7, 9, 4]
    ]

    assert suma_sub_matrice(matrice, 1, 1, 3, 3) == 38
    assert suma_sub_matrice(matrice, 2, 2, 4, 4) == 44
    assert suma_sub_matrice(matrice, 0, 0, 1, 1) == 14
    assert suma_sub_matrice(matrice, 0, 0, 4, 4) == 105

    print("Testele au trecut cu succes!")

if __name__ == '__main__':
    test_suma_sub_matrice()
    matrice = [[0, 2, 5, 4, 1],[4, 8, 2, 3, 7],[6, 3, 4, 6, 2],[7, 3, 1, 8, 3],[1, 5, 7, 9, 4]]
    print(suma_sub_matrice(matrice, 1, 1, 3, 3))
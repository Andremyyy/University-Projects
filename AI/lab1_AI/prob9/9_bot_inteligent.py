# Complexitate timp: O(n*m), pt ca parcurg matricea normal (metoda preprocesare_sume)
#                    O(1),  pt interogare (metoda suma_sub_matrice_optimizat)
# Complexitate spatiala: O(n*m), pt ca stochez matricea sumei prefizate


def preprocesare_sume(matrice):
    """
    Creează o matrice auxiliară pentru a calcula rapid suma sub-matricilor.
    """
    n, m = len(matrice), len(matrice[0])
    suma_p = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            suma_p[i][j] = (matrice[i-1][j-1] +
                            suma_p[i-1][j] + suma_p[i][j-1] -
                            suma_p[i-1][j-1])
    return suma_p

def suma_sub_matrice_optimizat(suma_p, p, q, r, s):
    """
    Calculează suma unei sub-matrici folosind matricea sumelor prefixate.
    """
    return (suma_p[r+1][s+1] - suma_p[p][s+1] -
            suma_p[r+1][q] + suma_p[p][q])

if __name__ == '__main__':
    matrice = [
        [0, 2, 5, 4, 1],
        [4, 8, 2, 3, 7],
        [6, 3, 4, 6, 2],
        [7, 3, 1, 8, 3],
        [1, 5, 7, 9, 4]
    ]

    suma_p = preprocesare_sume(matrice)
    print(suma_sub_matrice_optimizat(suma_p, 1, 1, 3, 3))
    print(suma_sub_matrice_optimizat(suma_p, 2, 2, 4, 4))

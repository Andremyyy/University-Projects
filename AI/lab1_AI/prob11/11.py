# Considerându-se o matrice cu n x m elemente binare (0 sau 1),
# să se înlocuiască cu 1 toate aparițiile elementelor egale cu 0 care sunt complet înconjurate de 1.
#
# De ex. matricea \
# [[1,1,1,1,0,0,1,1,0,1],
#  [1,0,0,1,1,0,1,1,1,1],
#  [1,0,0,1,1,1,1,1,1,1],
#  [1,1,1,1,0,0,1,1,0,1],
#  [1,0,0,1,1,0,1,1,0,0],
#  [1,1,0,1,1,0,0,1,0,1],
#  [1,1,1,0,1,0,1,0,0,1],
#  [1,1,1,0,1,1,1,1,1,1]]
# *devine *
# [[1,1,1,1,0,0,1,1,0,1],
#  [1,1,1,1,1,0,1,1,1,1],
#  [1,1,1,1,1,1,1,1,1,1],
#  [1,1,1,1,1,1,1,1,0,1],
#  [1,1,1,1,1,1,1,1,0,0],
#  [1,1,1,1,1,1,1,1,0,1],
#  [1,1,1,0,1,1,1,0,0,1],
#  [1,1,1,0,1,1,1,1,1,1]]

# marchez cu -1 toate elementele de nu trebuie modificate din 0 in 1
# (adica toate marginile si toate zero-urile de langa zeroruile de pe margine)

# Complexitate timp: O(n*m), pt ca parcurg matricea normal
# Complexitate spatiala: O(n*m), pt ca folosesc recursivitate (worst case scenario)

def transformare(matrice, n, m):
    """
        Înlocuiește toate elementele 0 care sunt complet înconjurate de 1 cu 1,
        păstrând celelalte elemente 0 care sunt conectate de margine, folosind DFS recursiv (Depth-First Search :
        exploreaza cât mai adânc posibil un drum înainte de a reveni și a încerca alte alternative)

        Metodă:
            1. Parcurgem marginile și marcăm toate elementele `0` accesibile cu `-1`.
            2. După marcaj, toate celelalte `0` din interior sunt transformate în `1`.
            3. Restaurăm `-1` în `0`.

        :param matrice: Lista de liste cu dimensiune n × m, având doar 0 și 1.
        :param n: Numărul de linii din matrice.
        :param m: Numărul de coloane din matrice.
        :return: Matricea modificată.
        """

    def marchez(i, j):
        if i<0 or i >= n or j<0 or j >= m or matrice[i][j] != 0:
            return
        matrice[i][j] = -1
        marchez(i+1, j)
        marchez(i, j+1)
        marchez(i-1, j)
        marchez(i, j-1)

    for i in range(n):
        if matrice[i][0] == 0:
            marchez(i, 0)
        if matrice[i][m-1] == 0:
            marchez(i, m-1)

    for j in range(m):
        if matrice[0][j] == 0:
            marchez(0, j)
        if matrice[n-1][j] == 0:
            marchez(n-1, j)

    # transform 0-urile accesibile in 1 si unde am -1 in 0 inapoi
    for i in range(n):
        for j in range(m):
            if matrice[i][j] == 0:
                matrice[i][j] = 1
            if matrice[i][j] == -1:
                matrice[i][j] = 0

    return matrice


def test_transformare():
    matrice1 = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    rezultat1 = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    assert transformare(matrice1, 3, 3) == rezultat1


    matrice2 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    rezultat2 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert transformare(matrice2, 3, 3) == rezultat2

    matrice3 = [
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]
    ]
    rezultat3 = [
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]
    ]
    assert transformare(matrice3, 4, 4) == rezultat3

    matrice4 = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    rezultat4 = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    assert transformare(matrice4, 3, 3) == rezultat4

    print("Testele au trecut cu succes!")

if __name__ == '__main__':
    test_transformare()
    matrice = [[1,1,1,1,0,0,1,1,0,1],
               [1,0,0,1,1,0,1,1,1,1],
               [1,0,0,1,1,1,1,1,1,1],
               [1,1,1,1,0,0,1,1,0,1],
               [1,0,0,1,1,0,1,1,0,0],
               [1,1,0,1,1,0,0,1,0,1],
               [1,1,1,0,1,0,1,0,0,1],
               [1,1,1,0,1,1,1,1,1,1]]
    transformare(matrice, 8, 10)
    for i in range(8):
        for j in range(10):
            print(matrice[i][j], end=" ")
        print()



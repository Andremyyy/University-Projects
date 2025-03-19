# Considerându-se o matrice cu n x m elemente binare (0 sau 1) sortate crescător pe linii,
# să se identifice indexul liniei care conține cele mai multe elemente de 1.
#
# De ex. în matricea
# [[0,0,0,1,1],
#  [0,1,1,1,1],
#  [0,0,1,1,1]]
# a doua linie conține cele mai multe elemente 1.

# Complexitate timp: O(n*m), pt ca parcurg matricea normal
# Complexitate spatiala: O(1), pt ca folosesc doar variabile simple

def index(matrice, n, m):
    """
    Determină indexul liniei dintr-o matrice binară (0 și 1) sortată crescător pe linii,
    care conține cele mai multe elemente de 1.

    Metodă:
        1. Se inițializează max cu -1 pentru a urmări numărul maxim de 1 găsit.
        2. Se inițializează imax cu -1 pentru a stoca indexul liniei corespunzătoare.
        3. Se parcurge fiecare linie, numărând câte elemente 1 conține.
        4. Dacă o linie conține mai multe 1 decât max, se actualizează max și imax.
        5. Se returnează imax, adică indexul liniei cu cele mai multe 1.

    :param matrice: listă de liste de numere binare (0 sau 1).
    :param n:  numărul de linii ale matricei.
    :param m: numărul de coloane ale matricei.
    :return:  un număr întreg reprezentând indexul liniei care conține cele mai multe 1.

    """
    max = 0
    imax = -1
    for i in range(0, n):
        contor = 0
        for j in range(0, m):
            contor += matrice[i][j]
        if contor>max:
            max = contor
            imax = i

    return imax

def test_index():

    matrice1 = [[0,0,1,1],
                [0,0,0,1],
                [0,1,1,1]]
    assert index(matrice1, 3, 4) == 2

    matrice2 = [[0,1],
                [1,1]]
    assert index(matrice2, 2, 2) == 1

    matrice3 = [[0,0,0],
                [0,0,0],
                [0,0,0]]
    assert index(matrice3, 3, 3) == -1

    print("Testele au trecut cu succes!")

if __name__ == '__main__':
    test_index()
    matrice = [[0,0,0,1,1],[0,1,1,1,1],[0,0,1,1,1]]
    print (index(matrice, 3, 5))
from collections import deque

# Complexitate timp: O(n*m), pt ca parcurg matricea normal
# Complexitate spatiala: O(min(n,m)), pt ca nu mai folosesc recursivitate

def transformare_optimizat(matrice, n, m):

    """
    Algoritmul primește o matrice binară (0 și 1) de dimensiune n x m și
    transformă toate elementele 0 care nu sunt conectate de un alt 0
    aflat pe marginea matricei (prin drumuri formate doar din 0) în 1.
    Se utilizează o abordare de tip BFS (Breadth-First Search)
    cu coadă (deque) pentru a evita recursivitatea și a optimiza consumul de memorie.

    :param matrice: o listă bidimensională de dimensiune n x m, conținând doar 0 și 1.
    :param n: numărul de linii ale matricei.
    :param m: numărul de coloane ale matricei.
    :return: matricea transformată conform regulilor menționate.
    """
    queue = deque()

    for i in range(n):
        if matrice[i][0] == 0:
            queue.append((i, 0))
        if matrice[i][m - 1] == 0:
            queue.append((i, m - 1))

    for j in range(m):
        if matrice[0][j] == 0:
            queue.append((0, j))
        if matrice[n - 1][j] == 0:
            queue.append((n - 1, j))

    while queue:
        i, j = queue.popleft()
        if 0 <= i < n and 0 <= j < m and matrice[i][j] == 0:
            matrice[i][j] = -1
            queue.extend([(i+1, j), (i-1, j), (i, j+1), (i, j-1)])

    for i in range(n):
        for j in range(m):
            if matrice[i][j] == 0:
                matrice[i][j] = 1
            if matrice[i][j] == -1:
                matrice[i][j] = 0

    return matrice

if __name__ == '__main__':
    matrice = [[1, 1, 1, 1, 0, 0, 1, 1, 0, 1],
               [1, 0, 0, 1, 1, 0, 1, 1, 1, 1],
               [1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 0, 0, 1, 1, 0, 1],
               [1, 0, 0, 1, 1, 0, 1, 1, 0, 0],
               [1, 1, 0, 1, 1, 0, 0, 1, 0, 1],
               [1, 1, 1, 0, 1, 0, 1, 0, 0, 1],
               [1, 1, 1, 0, 1, 1, 1, 1, 1, 1]]
    transformare_optimizat(matrice, 8, 10)
    for i in range(8):
        for j in range(10):
            print(matrice[i][j], end=" ")
        print()

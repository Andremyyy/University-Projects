
# Complexitate timp: O(n log m), pt ca folosesc cautare binara pt fiecare linie a matricii
# Complexitate spatiala: O(1), pt ca folosesc doar variabile simple

def index_optimizat(matrice, n, m):
    """
        Identifică indexul liniei cu cei mai mulți 1 folosind căutare binară.

        Metodă:
        - Deoarece liniile sunt sortate, utilizăm căutare binară pentru a găsi primul `1` în fiecare linie.
        - Numărul de `1` este calculat ca `m - poziția primului 1`.
        - Comparăm rezultatele și returnăm linia cu cei mai mulți `1`.

        :param matrice: Lista de liste de dimensiune n × m, conținând doar 0 și 1.
        :param n: Numărul de linii din matrice.
        :param m: Numărul de coloane din matrice.
        :return: Indexul liniei cu cei mai mulți 1.
        """

    def first_one_index(linie):

        """Găsește poziția primului 1 dintr-o linie folosind căutare binară."""

        left, right = 0, m - 1
        while left <= right:
            mid = (left + right) // 2
            if linie[mid] == 1:
                if mid == 0 or linie[mid - 1] == 0:
                    return mid
                right = mid - 1
            else:
                left = mid + 1
        return m

    max_ones = -1
    imax = -1
    for i in range(n):
        ones_count = m - first_one_index(matrice[i])
        if ones_count > max_ones:
            max_ones = ones_count
            imax = i

    return imax

if __name__ == '__main__':
    matrice = [[0, 0, 0, 1, 1], [0, 1, 1, 1, 1], [0, 0, 1, 1, 1]]
    print(index_optimizat(matrice, 3, 5))
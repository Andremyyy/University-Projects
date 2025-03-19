# Pentru un șir cu n elemente care conține valori din mulțimea {1, 2, ..., n - 1}
# astfel încât o singură valoare se repetă de două ori, să se identifice acea valoare care se repetă.
# De ex. în șirul [1,2,3,4,2] valoarea 2 apare de două ori.

# Complexitate timp: O(n log n), pt ca sortez cuvintele
# Complexitate spatiala: O(1), pt ca nu folosesc structuri de date suplimentare

def valoare_repetata(sir):
    """
        Identifică valoarea care se repetă de două ori într-un șir care conține numere de la 1 la n-1.

        :param sir: Listă de numere întregi unde un singur număr apare de două ori
        :return: Valoarea care se repetă
        """
    sir.sort()
    for i in range(len(sir)-1):
        if sir[i] == sir[i+1]:
            return sir[i]

def test_valoare_repetata():
    assert valoare_repetata([5, 1, 2, 3, 4, 5]) == 5
    assert valoare_repetata([7, 3, 2, 5, 1, 4, 6, 7]) == 7
    assert valoare_repetata([9, 8, 7, 6, 5, 4, 3, 2, 1, 8]) == 8
    print("Testele au trecut cu succes!")

if __name__ == '__main__':
    test_valoare_repetata()
    print(valoare_repetata([1,2,3,4,2]))